import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from prompts import SYSTEM_PROMPT
from config import available_functions, MAX_LOOPS
from functions.call_function import call_function
from helpers import verbose_flag
from typing import Any  # Fixed import

def main():
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    verbose = False
    # Initialize client
    client = genai.Client(api_key=api_key)
    # Get arguments passed in from command line
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python main.py <prompt> <optional flag>")
        sys.exit(1)
    user_prompt = args[0]
    flags = args[1:]
    for flag in flags:
        if flag == "--verbose":
            verbose = True
    # Setup list of messages
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    iter = 0
    while MAX_LOOPS > iter:
        (should_continue, final_response) = generate_content(client, messages, verbose)
        if not should_continue:
            print(final_response)
            break
        iter += 1

def generate_content(client, messages, verbose) -> tuple[bool, str]:
    # Send request to gemini and print response
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=SYSTEM_PROMPT
        )
    )

    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

    if response.function_calls:
        for call in response.function_calls:
            function_call_result = call_function(call, verbose)
            # result = parse_result(function_call_result)  # Removed unused variable assignment
            messages.append(function_call_result)  # Fixed - append the Content object, not parsed result
            if verbose:
                verbose_flag(call, function_call_result)

    final_response = response.text
    should_continue = bool(response.function_calls)
    return (should_continue, final_response)

def parse_result(result: types.Content) -> dict[str, Any] |None:
    if result.parts is not None and len(result.parts) > 0 and result.parts[0].function_response is not None and result.parts[0].function_response.response is not None:
        return result.parts[0].function_response.response
    return None

if __name__ == "__main__":  # Fixed syntax
    main()
