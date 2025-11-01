import os


def get_files_info(working_directory, directory="."):
    final = []
    try:
        absolute_path = os.path.abspath(os.path.join(working_directory, directory))
        files = os.listdir(absolute_path)
        formatted = ""
        if directory == '.':
            formatted = 'current'
        else:
            formatted = f"'{directory}'"
        final = [f"Result for {formatted} directory:"]
         
        if not absolute_path.startswith(os.path.realpath(working_directory)):
            raise Exception(f'Cannot list "{directory}" as it is outside the permitted working directory')

        if not os.path.isdir(absolute_path):
            raise Exception(f'"{directory}" is not a directory')
        files.sort()
        for file in files:
            abs_file = os.path.join(absolute_path, file)
            if os.path.isfile(abs_file):
                final.append(f"- {file}: file_size={os.path.getsize(abs_file)} bytes, is_dir={os.path.isdir(abs_file)}")

        for file in files:
            abs_file = os.path.join(absolute_path, file)
            if os.path.isdir(abs_file):
                final.append(f"- {file}: file_size={os.path.getsize(abs_file)} bytes, is_dir={os.path.isdir(abs_file)}")

        final_string = "\n".join(final)
        return final_string

    except Exception as e:
        final.append(f'Error: {e}')
        return "\n".join(final)


