import os
from functions.config import MAX_FILE_CONTENT

def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
         
        if not absolute_path.startswith(os.path.realpath(working_directory)):
            raise Exception(f'Cannot list "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(absolute_path):
            raise Exception(f'File not found or is not a regular file: "{file_path}"')

        with open(absolute_path, "r") as f:
            file_content_string = f.read()
            if len(file_content_string)>MAX_FILE_CONTENT:
                file_content_string = file_content_string[:10000] + f'[...File "{file_path}" truncated at 10000 characters]'

        
        return file_content_string

    except Exception as e:
        final = []
        final.append(f'Error: {e}')
        return "\n".join(final)
