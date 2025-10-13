import os
import sys
from dotenv import load_dotenv
from google import genai 
from google.genai import types
import argparse




load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def main():
    parser = argparse.ArgumentParser(description="A sample argument parser.")
    parser.add_argument('text_input', type=str, help="Question to pose to Gemini")
    parser.add_argument("--verbose", help="Enable verbose output", action="store_true")
    args = parser.parse_args()

    print("Hello from aiagent!")

    # Check to see if there is an actual question and place that into the model
    if args.text_input:
        question = args.text_input
        messages = [
            types.Content(role="user", parts=[types.Part(text=question)]),
        ]
        response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,)
        if args.verbose:
            print(f"User prompt: {question}")
            print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
            print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    else:
        print("Error: No argument provided.", file=sys.stderr)
        sys.exit(1)
        
    print(response.text)
if __name__ == "__main__":
    main()
