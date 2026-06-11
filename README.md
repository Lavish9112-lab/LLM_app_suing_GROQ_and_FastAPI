
# 🚀 Llama 3 Translation API using Groq, LangChain & FastAPI

A Language Translation API built using Meta's Llama 3.3 70B model, Groq's high-speed inference platform, LangChain, FastAPI, and LangServe.

This project allows users to translate text into any target language through a REST API endpoint. It demonstrates how to integrate Large Language Models (LLMs) into production-ready applications using modern AI frameworks.

---

## 📖 Overview

This application accepts input text and a target language, sends the request to Meta's Llama 3.3 70B model through Groq, and returns the translated output.

The project showcases:

- LLM Integration using Groq
- Prompt Engineering with LangChain
- API Development using FastAPI
- LangServe Deployment
- REST API Design

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | Backend API Framework |
| LangChain | LLM Orchestration |
| Groq | LLM Inference Provider |
| Meta Llama 3.3 70B | Language Model |
| LangServe | API Deployment |
| Uvicorn | ASGI Server |

---

## ✨ Features

- 🌍 Translate text into multiple languages
- ⚡ Fast inference using Groq
- 🤖 Powered by Meta Llama 3.3 70B
- 🔗 LangChain prompt pipelines
- 📚 Interactive API documentation
- 🚀 LangServe Playground support

---

## 🏗️ System Architecture

```text
User Request
      │
      ▼
 FastAPI Endpoint
      │
      ▼
LangChain Prompt
      │
      ▼
Groq API
      │
      ▼
Meta Llama 3.3 70B
      │
      ▼
Translated Response
```

---

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/llama3-groq-translation-api.git

cd llama3-groq-translation-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Application will run at:

```text
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

### LangServe Playground

```text
http://127.0.0.1:8000/chain/playground
```

### OpenAPI Specification

```text
http://127.0.0.1:8000/openapi.json
```

---

## 💻 Example Request

### Input

```json
{
  "language": "French",
  "text": "How are you?"
}
```

### Output

```json
{
  "output": "Comment allez-vous ?"
}
```

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

- Building LLM-powered applications
- Working with Meta Llama models
- Integrating Groq APIs
- Prompt engineering with LangChain
- Developing REST APIs using FastAPI
- Deploying AI services using LangServe

---

## 🚀 Future Improvements

- Language auto-detection
- Speech-to-Text integration
- Text-to-Speech support
- Docker containerization
- User authentication
- Translation history storage
- Multi-model support

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Devender Kumar Yadav**

Chemical Engineering Undergraduate | AI & Generative AI Enthusiast


---
⭐ If you found this project useful, consider giving it a star.
