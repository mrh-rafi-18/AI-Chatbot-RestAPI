# AI Chatbot REST API (FastAPI + Groq + DummyJSON)

## 📌 Overview
This project implements a RESTful chatbot backend that uses the Groq LLM API to provide human-like responses about products fetched from DummyJSON.

## 🚀 Features
- Fetch products from DummyJSON API with the help of LLM which is binded with several langchain tools. LLM decides which tool to use and uses that tool to fetch the data.
- Converts the JSON data in human readable format with the help of LLM.
- Natural language chat powered by Groq LLaMA model
- Context-aware chatbot responses
- Modular FastAPI structure

## 🧩 Endpoints
- `GET /api/products` → Fetch all DummyJSON products
- `POST /api/chat` → Send a message to the chatbot

Example request:
{
  "message": "Tell me more about iPhone 9"
}

Example response:
{
  "response": "The iPhone 9 is a premium smartphone by Apple, priced at $549, rated 4.7 stars, and currently in stock."
}

## 🛠️ Run Locally
1. Create `.env` and add your Groq key:
   GROQ_API_KEY=your_groq_api_key_here

2. Create a virtual environment. And activate it.

2. Install dependencies:
   pip install -r requirements.txt

3. Start the server:
   uvicorn app.main:app --reload

4. Open in browser:
   http://127.0.0.1:8000/docs
