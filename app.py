import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are a professional sales assistant.

Write a follow-up email based ONLY on the input.

Rules:
- Be professional and concise
- Do NOT invent facts
- If unsure, stay general

Output format:

SUBJECT:
...

EMAIL:
...

REVIEW FLAG:
Yes/No

REVIEW NOTE:
...
"""

def read_input(file):
    return Path(file).read_text()

def save_output(text):
    Path("outputs").mkdir(exist_ok=True)
    filename = f"outputs/output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    Path(filename).write_text(text)
    return filename

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "sample_input.txt"

    user_input = read_input(input_file)

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(
        SYSTEM_PROMPT + "\n\nINPUT:\n" + user_input
    )

    output = response.text

    print("\n=== OUTPUT ===\n")
    print(output)

    file_path = save_output(output)
    print(f"\nSaved to: {file_path}")

if __name__ == "__main__":
    main()