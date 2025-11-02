import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Initialize client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
)

def summarize_codebase(summary_text: str) -> str:
    """Ask the LLM (Groq API) to summarize the repository clearly."""
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Groq free model
            messages=[
                {"role": "system", "content": "You are Codebase Genius AI — an expert that summarizes GitHub repositories."},
                {"role": "user", "content": f"Summarize this repository in simple, clear language:\n{summary_text}"}
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ AI summarization failed: {e}"
