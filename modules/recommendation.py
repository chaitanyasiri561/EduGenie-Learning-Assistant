import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

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

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"⚠️ Error in Recommendation: {e}"