from dotenv import load_dotenv
load_dotenv()

from modules.qa import answer_question_with_gemini

if __name__ == "__main__":
    question = "What is photosynthesis?"
    answer = answer_question_with_gemini(question)
    print("Question:", question)
    print("Answer:", answer)