from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.chatbot import ask_gemini
from app.utils import validate_input

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://aberetruphenah.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Savor Chatbot backend is running!"}



@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    if not validate_input(req.message):
        return {"error": "Please asl a valid question."}
    
    try:
        reply = ask_gemini(req.message)
        return {"response": reply}
    except Exception as e:
        return {"error": "Something went wrong while generating a response."}