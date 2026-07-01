from fastapi import FastAPI

from api.chat import router as chat_router

app = FastAPI(
    title="DevMind AI",
    version="1.0.0"
)

app.include_router(chat_router)


@app.get("/")
def health():

    return {
        "status": "Running",
        "model": "Qwen2.5-Coder 7B"
    }