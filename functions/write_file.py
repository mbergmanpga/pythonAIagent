import os
from google.genai import types

def write_file(working_directory, file_path, content):
    """
    Write content to a file, creating it if it doesn't exist.
    
    Args:
        working_directory: The base directory that restricts where we can access
        file_path: Relative path to the file within the working_directory
        content: The content to write to the file
    
    Returns:
        A success message string or an error message string
    """
    try:
        # Create the full path by joining working_directory and file_path
        full_path = os.path.join(working_directory, file_path)
        
        # Get absolute paths to ensure we're comparing normalized paths
        abs_full_path = os.path.abspath(full_path)
        abs_working_directory = os.path.abspath(working_directory)
        
        # Security check: ensure the requested path is within working_directory
        if not abs_full_path.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Create parent directories if they don't exist
        parent_dir = os.path.dirname(abs_full_path)
        # Only create directories if parent_dir exists and is not the working directory itself
        if parent_dir and parent_dir != abs_working_directory:
            if not os.path.exists(parent_dir):
                os.makedirs(parent_dir)
        
        # Write the content to the file
        with open(abs_full_path, "w") as f:
            f.write(content)
        
        # Return success message
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        # Catch any other errors and return them as a string
        return f"Error: {str(e)}"

# Function schema for the LLM
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the specified content, constrained to the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)
