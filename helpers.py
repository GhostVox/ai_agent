def print_token_count_response_count(response):
    prompt_tokens  = getattr(response.usage_metadata, 'prompt_token_count', None)
    response_tokens = getattr(response.usage_metadata, 'candidates_token_count', None)
    print("Prompt tokens:", prompt_tokens)
    print("Response tokens:", response_tokens)

def verbose_flag(user_prompt, response):
    print("User prompt:", user_prompt)
    print_token_count_response_count(response)
