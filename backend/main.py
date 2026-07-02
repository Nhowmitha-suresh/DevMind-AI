from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.chat import router as chat_router
from backend.api.health import router as health_router

app = FastAPI(
    title="DevMind AI API",
    description="AI-powered developer assistant",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(chat_router)
app.include_router(health_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to DevMind AI 🚀",
        "docs": "/docs"
    }