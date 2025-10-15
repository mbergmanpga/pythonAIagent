import os
from config import MAX_FILE_CHARS


def get_file_content(working_directory, file_path):
    """
    Read and return the contents of a file.
    
    Args:
        working_directory: The base directory that restricts where we can access
        file_path: Relative path to the file within the working_directory
    
    Returns:
        A string containing the file contents (truncated if necessary) or an error message
    """
    try:
        # Create the full path by joining working_directory and file_path
        full_path = os.path.join(working_directory, file_path)
        
        # Get absolute paths to ensure we're comparing normalized paths
        abs_full_path = os.path.abspath(full_path)
        abs_working_directory = os.path.abspath(working_directory)
        
        # Security check: ensure the requested path is within working_directory
        if not abs_full_path.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if the path is actually a file
        if not os.path.isfile(abs_full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read the file contents
        with open(abs_full_path, "r") as f:
            file_content = f.read(MAX_FILE_CHARS)
        
        # Check if we need to read more to see if truncation is needed
        with open(abs_full_path, "r") as f:
            full_content = f.read(MAX_FILE_CHARS + 1)
        
        # If the file is longer than MAX_FILE_CHARS, truncate and add message
        if len(full_content) > MAX_FILE_CHARS:
            return file_content + f'[...File "{file_path}" truncated at {MAX_FILE_CHARS} characters]'
        
        return file_content
    
    except Exception as e:
        # Catch any other errors and return them as a string
        return f"Error: {str(e)}"
