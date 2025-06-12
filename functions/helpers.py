import os
Err = str

def check_file_path(working_directory: str, file_path: str) -> tuple[str, Err | None]:
    working_directory_path = os.path.abspath(working_directory)
    full_file_path = os.path.join(working_directory_path, file_path)
    abs_file_path = os.path.abspath(full_file_path)
    if not (abs_file_path.startswith(working_directory_path + os.sep) or abs_file_path == working_directory_path):
        err = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        return "", err
    return abs_file_path, None  # Return absolute path, not original file_path

def check_directory_path(working_directory: str, directory_path: str) -> tuple[str, Err | None]:
    working_directory_path = os.path.abspath(working_directory)  # Fixed: was directory_path
    full_dir_path = os.path.join(working_directory_path, directory_path)
    abs_directory_path = os.path.abspath(full_dir_path)

    # Add os.sep to prevent partial matches and handle exact match case
    if not (abs_directory_path.startswith(working_directory_path + os.sep) or abs_directory_path == working_directory_path):
        err = f'Error: Cannot access "{directory_path}" as it is outside the permitted working directory'
        return "", err
    return abs_directory_path, None  # Return absolute path
