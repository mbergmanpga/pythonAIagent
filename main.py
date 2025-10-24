import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai import types
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file, schema_run_python_file
import argparse




load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

def main():
    parser = argparse.ArgumentParser(description="A sample argument parser.")
    parser.add_argument('text_input', type=str, help="Question to pose to Gemini")
    parser.add_argument("--verbose", help="Enable verbose output", action="store_true")
    args = parser.parse_args()


    # Check to see if there is an actual question and place that into the model
    if args.text_input:
        question = args.text_input
        messages = [
            types.Content(role="user", parts=[types.Part(text=question)]),
        ]
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt),
        )

        if args.verbose:
            print(f"User prompt: {question}")
            print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
            print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    else:
        print("Error: No argument provided.", file=sys.stderr)
        sys.exit(1)
        
    if response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'function_call') and part.function_call:
                function_call_part = part.function_call
                print(f"Calling function: {function_call_part.name}({dict(function_call_part.args)})")
            elif hasattr(part, 'text') and part.text:
                print(part.text)


if __name__ == "__main__":
    main()
