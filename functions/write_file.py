import os


def write_file(working_directory:str, file_path, content:str)->str:
    working_directory_path = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory_path, file_path)
    abs_file_path = os.path.abspath(file_path)
    if not  abs_file_path.startswith(working_directory_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(abs_file_path):
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write to "{file_path}": {str(e)}'
