# 🎓 EduGenie

An AI-powered educational assistant that helps students learn efficiently using Generative AI. EduGenie provides intelligent Question Answering, Concept Explanation, Quiz Generation, Notes Summarization, and Personalized Learning Recommendations through a clean web interface.

Built using **FastAPI, HTML, CSS, JavaScript, Jinja2, Google Gemini 2.5 Flash, and LaMini-Flan-T5.**

---

# 📌 Features

- ❓ AI-based Question Answering
- 📖 Concept Explanation
- 📝 Automatic Quiz Generation
- 📄 Notes Summarization
- 🎯 Personalized Learning Recommendations
- ⚡ FastAPI Backend
- 🎨 Responsive Web Interface
- 🤖 Google Gemini 2.5 Flash Integration
- 📚 LaMini-Flan-T5 for Concept Explanation
- 🧪 Individual Module Testing

---

# 🏗️ System Architecture

```
                 User
                   │
                   ▼
       HTML + CSS + JavaScript
             (Jinja2 Templates)
                   │
                   ▼
             FastAPI Backend
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
Google Gemini 2.5 Flash    LaMini-Flan-T5
(Q&A, Quiz, Summary,      (Explanation)
Recommendations)
        │                     │
        └──────────┬──────────┘
                   ▼
        AI Generated Educational Response
                   │
                   ▼
             Display to User
```

---

# 📂 Project Structure

```
EduGenie/
│
├── modules/
│   ├── __init__.py
│   ├── qa.py
│   ├── explanation.py
│   ├── quiz.py
│   ├── summary.py
│   └── recommendation.py
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
│
├── test.py
├── test_explanation.py
├── test_quiz.py
├── test_summary.py
└── test_recommendation.py
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend API |
| HTML5 | User Interface |
| CSS3 | Styling |
| JavaScript | Client-side Interaction |
| Jinja2 | Template Rendering |
| Google Gemini 2.5 Flash | Q&A, Quiz, Summary, Recommendations |
| LaMini-Flan-T5 | Concept Explanation |
| Transformers | NLP Model Loading |
| Python | Backend Development |
| Uvicorn | FastAPI Server |
| Git & GitHub | Version Control |

---

# 🚀 Installation

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

```bash
cd EduGenie
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment

Create a `.env` file and add your API key.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Project

```bash
uvicorn main:app --reload
```

Application runs at

```
http://127.0.0.1:8000
```

---

# 🧪 Running Tests

Run complete testing

```bash
python test.py
```

Run individual modules

```bash
python test_explanation.py

python test_quiz.py

python test_summary.py

python test_recommendation.py
```

---

# 📷 Application Screenshots

## 🏠 Home Page

![Home Page](images/home.png)

---

## ❓ Question Answering

![Question Answering](images/question_answer.png)

---

## 📖 Concept Explanation

![Explanation](images/explanation.png)

---

## 📝 Quiz Generation

![Quiz](images/quiz.png)

---

## 📄 Notes Summarization

![Summary](images/summary.png)

---

## 🎯 Learning Recommendations

![Recommendation](images/recommendation.png)

---

# 🌟 Future Enhancements

- 👤 User Login & Authentication
- 📂 PDF Upload Support
- 🎙️ Voice Assistant
- 🌐 Multi-language Support
- 📈 Student Progress Dashboard
- ☁️ Cloud Deployment
- 📱 Mobile Responsive UI
- 💾 Database Integration

---

# 👨‍💻 Developer

**Guduru Chaitanya Siri**

B.Tech Computer Science & Engineering

SRM University AP

Google Cloud GenAI Internship Project

GitHub:
https://github.com/YOUR_USERNAME

---

# 📜 License

This project was developed as part of the Google Cloud Generative AI Internship for educational purposes.
