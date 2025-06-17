import sys
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if len(sys.argv) < 2:
    print("Error: You must provide a prompt as a command-line argument.")
    sys.exit(1)

verbose = "--verbose" in sys.argv

# Remover --verbose dos argumentos se estiver presente
args = [arg for arg in sys.argv[1:] if arg != "--verbose"]

if len(args) == 0:
    print("Error: You must provide a prompt as a command-line argument.")
    sys.exit(1)

prompt = args[0]

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=prompt
)

if verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)