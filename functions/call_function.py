from .get_files_info import get_files_info
from .get_file_content import get_file_content
from .run_python import run_python_file
from .write_file import write_file
from google.genai import types

def call_function(function_call:types.FunctionCall, verbose=False):
    function_name = function_call.name
    function_args = function_call.args
    if function_args is None:
        function_args = {}

    function_args["working_directory"] = "./calculator"

    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_call.name}")
    match function_name:
        case "get_files_info":
            result = get_files_info(**function_args)
            return build_response(function_name, result)
        case "get_file_content":
            result = get_file_content(**function_args)
            return build_response(function_name, result)
        case "run_python_file":
            result = run_python_file(**function_args)
            return build_response(function_name, result)
        case "write_file":
            result = write_file(**function_args)
            return build_response(function_name, result)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_name,
                        response={"error": f"Unknown function: {function_name}"},
                    )
                ],
            )

def build_response(function_name:str, function_result:str):
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
