from fastapi import FastAPI
from app.database import init_db
from app.models import Message
from app.schemas import MessageCreate, MessageResponse
from app.services.chat import create_chat_message, get_chat_messages

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.post("/chat/", response_model=MessageResponse)
async def create_message(message: MessageCreate):
    return await create_chat_message(message)

@app.get("/messages/", response_model=list[MessageResponse])
async def get_messages(skip: int = 0, limit: int = 10):
    return await get_chat_messages(skip, limit)