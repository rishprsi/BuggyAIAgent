import os
import subprocess
import signal

def run_python_file(working_directory, file_path, args=[]):
    try:
        signal.alarm(30)
        absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
         
        if not absolute_path.startswith(os.path.realpath(working_directory)):
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(absolute_path):
            return (f'Error: File "{file_path}" not found.')

        if len(file_path)<3 or file_path[-3:]!=".py":
            return (f'Error: "{file_path}" is not a Python file.')

        new_args = ["python",absolute_path]
        new_args.extend(args)
        result = subprocess.run(new_args, capture_output=True)
        print(result)
        final_content_string = ""
        if result.stdout:
            final_content_string= f"STDOUT: {result.stdout}\n"
        if result.stderr:
            final_content_string += f"STDERR: {result.stderr}"
        return final_content_string

    except Exception as e:
        final = f"Error: executing Python file: {e}"
        return final
