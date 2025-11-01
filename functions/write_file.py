import os

def write_file(working_directory, file_path, content):
    try:

        absolute_path = os.path.abspath(os.path.join(working_directory, file_path))
         
        if not absolute_path.startswith(os.path.realpath(working_directory)):
            raise Exception(f'Cannot write to "{file_path}" as it is outside the permitted working directory')

        with open(absolute_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        final = []
        final.append(f'Error: {e}')
        return "\n".join(final)

