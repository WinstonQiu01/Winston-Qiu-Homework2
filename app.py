import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT = "Write a short professional sales follow-up email from these notes:"

def read_input(file):
    return Path(file).read_text(encoding="utf-8")

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "sample_input.txt"
    user_input = read_input(input_file)

    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(
        f"{PROMPT}\n\n{user_input}"
    )

    print("\n=== OUTPUT ===\n")
    print(response.text)

if __name__ == "__main__":
    main()