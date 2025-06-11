import os
Err = str
def check_file_path(working_directory:str, file_path:str) -> tuple[str, Err | None]:
    working_directory_path = os.path.abspath(working_directory)
    file_path = os.path.join(working_directory_path, file_path)
    if not working_directory in os.path.abspath(file_path):
        err = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        return "" , err
    return file_path, None

def check_directory_path(working_directory:str, directory_path:str) -> tuple[str, Err | None]:
    working_directory_path = os.path.abspath(working_directory)
    directory_path = os.path.join(working_directory_path, directory_path)
    if not working_directory in os.path.abspath(directory_path):
        err = f'Error: Cannot access "{directory_path}" as it is outside the permitted working directory'

        return "", err

    return directory_path, None
