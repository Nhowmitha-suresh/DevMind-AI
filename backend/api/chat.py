from fastapi import APIRouter

from models.chat import ChatRequest
from services.llm_service import LLMService

router = APIRouter(
    prefix="/api",
    tags=["Chat"]
)


@router.post("/chat")
def chat(request: ChatRequest):

    reply = LLMService.generate(request.message)

    return {
        "response": reply
    }