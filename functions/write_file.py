import os
from functions.helpers import check_file_path


def write_file(working_directory:str, file_path, content:str)->str:
    abs_file_path, err = check_file_path(working_directory, file_path)
    if err:
        return err
    try:
        if not os.path.exists(abs_file_path):
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        with open(abs_file_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write to "{file_path}": {str(e)}'
