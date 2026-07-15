import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_quiz(topic):
    try:
        prompt = f"""
Generate a short quiz about {topic}.

Requirements:
- 5 multiple-choice questions
- Each question should have 4 options (A, B, C, D)
- Mention the correct answer after each question.
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"⚠ Error in Quiz: {e}"
