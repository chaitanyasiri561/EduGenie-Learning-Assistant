import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def summarize_text(text):
    try:
        prompt = f"Summarize the following text in simple language:\n\n{text}"

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"⚠ Error in Summary: {e}"