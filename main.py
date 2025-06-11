import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from config import SYSTEM_PROMPT, available_functions
from functions.call_function import call_function


def print_token_count_response_count(response):
    prompt_tokens  = getattr(response.usage_metadata, 'prompt_token_count', None)
    response_tokens = getattr(response.usage_metadata, 'candidates_token_count', None)
    print("Prompt tokens:", prompt_tokens)
    print("Response tokens:", response_tokens)

def verbose_flag(user_prompt, response):
    print("User prompt:", user_prompt)
    print_token_count_response_count(response)

def main():
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    verbose = False
    # Initialize client
    client = genai.Client(api_key=api_key)

    # Get arguments passed in from command line
    args = sys.argv[1:]
    if  len(args)==0:
        print("Usage: python main.py <prompt> <optional flag>")
        sys.exit(1)

    user_prompt = args[0]
    flags = args[1:]

     # Setup list of messages
    messages = [
         types.Content(role="user", parts=[types.Part(text=user_prompt)]),
     ]

    # Send request to gemini and print response
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages, config=types.GenerateContentConfig( tools=[available_functions],system_instruction=SYSTEM_PROMPT))

    for flag in flags:
      if flag == "--verbose":
          verbose = True

    if response.function_calls:
       for call in response.function_calls:
           function_call_result = call_function(call,verbose)
           if function_call_result.parts is not None and len(function_call_result.parts) > 0 and function_call_result.parts[0].function_response is not None and function_call_result.parts[0].function_response.response is not None:
               print(f"-> {function_call_result.parts[0].function_response.response}")


    if response.text:
        print("Response:")
        print(response.text)



if __name__ == "__main__":
    main()
