import subprocess
import os

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        command = ["python", abs_file_path]
        if args:
            command += args
        result = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )
        output = result.stdout.strip()
        error = result.stderr.strip()
        return {
            "returncode": result.returncode,
            "stdout": output,
            "stderr": error,
        }
    except Exception as e:
        return f"Error running file: {e}"

# --- Add this for the schema ---
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a Python file, optionally with arguments",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Relative path to the file to execute"
            },
            "args": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of arguments for the script (optional)"
            }
        },
        "required": ["file_path"]
    }
)
