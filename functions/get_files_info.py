import os
from functions.helpers import check_directory_path

def get_files_info(working_directory, directory = None)->str:
    if directory is None:
        directory = working_directory

    try:
        directory_path, err  = check_directory_path(working_directory,directory)
        if err:
            return err

        directory_list = os.listdir(directory_path)
        contents = ""
        for file in directory_list:
            file_path = os.path.join(directory_path, file)
            contents += f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
        return contents
    except Exception as e:
        return f'Error: {str(e)}'
