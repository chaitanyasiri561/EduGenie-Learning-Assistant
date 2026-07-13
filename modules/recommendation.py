import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


def get_learning_recommendations(topic):
    try:
        prompt = f"""
You are an AI tutor.

Create a learning path for the topic: {topic}

Include:
1. Beginner concepts
2. Intermediate concepts
3. Advanced concepts
4. Recommended books
5. Recommended YouTube channels
6. Helpful websites
"""

        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"⚠️ Error in Recommendation: {e}"
