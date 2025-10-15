from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chatbot_service import generate_chatbot_response
from app.services.product_service import fetch_all_products

router = APIRouter(prefix="/api", tags=["Chatbot"])

@router.get("/products")
def get_products():
    """Fetch all products from DummyJSON API."""
    return fetch_all_products()

@router.post("/chat", response_model=ChatResponse)
def chat_with_bot(request: ChatRequest):
    """Accepts user query and returns chatbot response."""
    response_text = generate_chatbot_response(request.message)
    return {"response": response_text}
