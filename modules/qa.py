import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def answer_question_with_gemini(question):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=question,
        )
        return response.text
    except Exception as e:
        return f"⚠ Error in QnA: {e}"