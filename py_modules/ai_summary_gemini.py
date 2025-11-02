import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def summarize_codebase(text: str) -> str:
    """
    Generate a natural language summary of the provided repository text
    using Google's Gemini model.
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            f"Summarize this repository clearly and concisely for a developer:\n\n{text}"
        )
        return response.text.strip() if response.text else "⚠️ No summary returned."
    except Exception as e:
        return f"⚠️ Gemini summarization failed: {e}"
