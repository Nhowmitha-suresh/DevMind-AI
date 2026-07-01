from fastapi import FastAPI
from api.chat import router as chat_router

app = FastAPI(
    title="DevMind AI",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "status": "Running",
        "app": "DevMind AI"
    }