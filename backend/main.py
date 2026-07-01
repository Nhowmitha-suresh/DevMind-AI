from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI(
    title="DevMind AI",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "status": "Running",
        "app": "DevMind AI"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    response = ollama.chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "response": response["message"]["content"]
    }