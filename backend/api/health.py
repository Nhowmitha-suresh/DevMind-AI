from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
async def health():
    return {
        "status": "healthy",
        "application": "DevMind AI",
        "version": "1.0.0"
    }


@router.get("/ping")
async def ping():
    return {
        "message": "pong"
    }