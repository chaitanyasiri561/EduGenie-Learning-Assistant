import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_quiz(topic):
    try:
        prompt = f"""
Generate a short quiz about {topic}.

Requirements:
- 5 multiple-choice questions
- Each question should have 4 options (A, B, C, D)
- Mention the correct answer after each question.
"""

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"⚠️ Error in Quiz: {e}"
