from fastapi import FastAPI
from app.api.routes_chatbot import router as chatbot_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AI Chatbot API using Groq LLM and DummyJSON data."
)

app.include_router(chatbot_router)

@app.get("/")
def root():
    return {"message": "Welcome to the AI Chatbot API!"}
