import os
from functions.helpers import check_file_path
import subprocess

def run_python_file(working_directory:str, file_path:str):
    file, err = check_file_path(working_directory, file_path)
    if err:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(file):
        return f'Error: File "{file_path}" not found.'
    if not file.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    command = ["python", file]
    try:
        result= subprocess.run(command,capture_output=True, timeout=30 , cwd=working_directory)

        output = f'STDOUT: {result.stdout.decode("utf-8")}\nSTDERR: {result.stderr.decode("utf-8")}'
        if result.returncode != 0:
            return f'{output}\nProcess exited with code {result.returncode}'
        if len(result.stdout) == 0 and len(result.stderr) == 0:
            return "No output produced."
        return output
    except Exception as e:
        return f'Error: executing Python file: {e}'
