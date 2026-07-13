from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from modules.qa import answer_question_with_gemini
from modules.explanation import explain_topic
from modules.quiz import generate_quiz
from modules.summary import summarize_text
from modules.recommendation import get_learning_recommendations

load_dotenv()

app = FastAPI(title="EduGenie - Google Gemini Powered Learning Assistant")

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"response": "", "query": "", "query_type": "qa"}
    )


@app.post("/", response_class=HTMLResponse)
async def process_query(
    request: Request,
    query: str = Form(...),
    query_type: str = Form(...)
):
    if query_type == "qa":
        response = answer_question_with_gemini(query)
    elif query_type == "explanation":
        response = explain_topic(query)
    elif query_type == "quiz":
        response = generate_quiz(query)
    elif query_type == "summary":
        response = summarize_text(query)
    elif query_type == "recommendation":
        response = get_learning_recommendations(query)
    else:
        response = "⚠️ This feature isn't implemented yet."

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"response": response, "query": query, "query_type": query_type}
    )


@app.get("/health")
async def health_check():
    return {
        "message": "Welcome to EduGenie! FastAPI is running successfully 🚀"
    }