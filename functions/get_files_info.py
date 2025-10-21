import os
from google.genai import types


def get_files_info(working_directory, directory="."):
    """
    List the contents of a directory with the file metadata.

    Args:
        working_directory: The base directory that restricts where we can access
        directory: Relative path within the working directory (default is "."

    Returns:
        A string representing the directory contents or an error message
    """

    try:
        full_path = os.path.join(working_directory, directory)

        abs_full_path = os.path.abspath(full_path)
        abs_working_directory = os.path.abspath(working_directory)

        if not abs_full_path.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_full_path):
            return f'Error: "{directory}" is not a directory'

        contents = os.listdir(abs_full_path)

        result_lines = []
        for item in contents:
            item_path = os.path.join(abs_full_path, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            result_lines.append(f" - {item}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(result_lines)

    except Exception as e:
        return f"Error: {str(e)}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
