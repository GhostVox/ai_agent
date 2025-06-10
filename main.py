import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def print_token_count_response_count(response):
    prompt  = getattr(response.usage_metadata, 'prompt_token_count', None)
    response = getattr(response.usage_metadata, 'candidates_token_count', None)
    print("Prompt tokens:", prompt)
    print("Response tokens:", response)

def verbose_flag(user_prompt, response):
    print("User prompt:", user_prompt)
    print_token_count_response_count(response)

def main():
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

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
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)

    for flag in flags:
      if flag == "--verbose":
          verbose_flag(user_prompt, response)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
