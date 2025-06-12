def print_token_count_response_count(response):
    prompt_tokens  = getattr(response.usage_metadata, 'prompt_token_count', None)
    response_tokens = getattr(response.usage_metadata, 'candidates_token_count', None)
    print("Prompt tokens:", prompt_tokens)
    print("Response tokens:", response_tokens)

def verbose_flag(call,call_result,  response):
    print("Ai called:", call.name)
    print("Call result:", call_result)
    print_token_count_response_count(response)
