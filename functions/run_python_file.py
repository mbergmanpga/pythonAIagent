import os
import subprocess

   
def run_python_file(working_directory, file_path, args=[]):

    """
    Runs a pythong file in the direcrory.
    
    Args:
        working_directory: The base directory that restricts where we can access
        file_path: Relative path to the file within the working_directory
        args: additional command-line arguments to pass to the script
    
    Returns:
        A string containing the execution output of an error message
    """

    try:
        # Create the full path by joining working_directory and file_path
        full_path = os.path.join(working_directory, file_path)
        
        # Get absolute paths to ensure we're comparing normalized paths
        abs_full_path = os.path.abspath(full_path)
        abs_working_directory = os.path.abspath(working_directory)

        # Security check: ensure the requested path is within working_directory
        if not abs_full_path.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # Check if the file exists
        if not os.path.exists(abs_full_path):
            return f'Error: File "{file_path}" not found.'
        
        # Check if the file is a Python file
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        # Execute the Python file
        completed_process = subprocess.run(
            ["python", abs_full_path] + args,
            cwd=abs_working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Build the output string
        output_parts = []
        
        if completed_process.stdout:
            output_parts.append(f"STDOUT:\n{completed_process.stdout}")
        
        if completed_process.stderr:
            output_parts.append(f"STDERR:\n{completed_process.stderr}")
        
        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")
        
        # If no output was produced
        if not output_parts:
            return "No output produced."
        
        return "\n".join(output_parts)
    
    except subprocess.TimeoutExpired:
        return "Error: Python file execution timed out after 30 seconds"
    except Exception as e:
        return f"Error: executing Python file: {e}"
