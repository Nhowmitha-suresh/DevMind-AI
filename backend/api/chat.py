from fastapi import APIRouter, HTTPException

from backend.models.chat import ChatRequest, ChatResponse
from backend.services.llm_service import llm_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat endpoint for DevMind AI.
    """

    try:
        response = llm_service.generate_response(request.message)

        return ChatResponse(
            response=response
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )