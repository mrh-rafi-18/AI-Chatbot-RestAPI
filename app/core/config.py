import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "AI Chatbot API"
    VERSION: str = "1.0.0"
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    DUMMYJSON_API_URL: str = "https://dummyjson.com/products"

settings = Settings()
