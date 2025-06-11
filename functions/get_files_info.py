import os


def get_files_info(working_directory, directory = None):
    if directory is None:
        directory = working_directory

    try:
        working_directory_path = os.path.abspath(working_directory)
        directory_path = os.path.join(working_directory_path, directory)
        abs_directory_path = os.path.abspath(directory_path)
        if not abs_directory_path.startswith(working_directory_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'


        if not os.path.isdir(directory_path):
            return f'Error: "{directory}" is not a directory'
        directory_list = os.listdir(directory_path)
        contents = ""
        for file in directory_list:
            file_path = os.path.join(directory_path, file)
            contents += f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
        return contents
    except Exception as e:
        return f'Error: {str(e)}'
