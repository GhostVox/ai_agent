import os
from functions.helpers import check_file_path
from config import MAX_CHARS
def get_file_content(working_directory,file_path)->str:

    file, err = check_file_path(working_directory,file_path)
    if not err== None:
       return err

    try:
        if os.path.getsize(file) > MAX_CHARS:
            with open(file_path, 'r') as file:
                content = file.read(MAX_CHARS)
                return content + f'\n[...File "{file}" truncated at "{MAX_CHARS}" characters]\n'
        else:
            with open(file, 'r') as file:
                content = file.read()
                return content
    except Exception as e:
        return f'Error: Cannot read "{file}" due to an error: {str(e)}'
