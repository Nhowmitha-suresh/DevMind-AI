from fastapi import APIRouter
from models.chat import ChatRequest
from services.ollama_service import generate_response

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):
    reply = generate_response(request.message)
    return {"response": reply}