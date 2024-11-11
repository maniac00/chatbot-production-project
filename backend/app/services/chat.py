from sqlalchemy.future import select
from app.database import AsyncSessionLocal
from app.models import Message
from app.schemas import MessageCreate
import openai
import asyncio
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv('OPENAI_API_KEY')

async def create_chat_message(message: MessageCreate):
    async with AsyncSessionLocal() as session:
        response = await asyncio.to_thread(
            openai.ChatCompletion.create,
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message.content}]
        )
        
        db_message = Message(content=message.content, response=response.choices[0].message.content)
        session.add(db_message)
        await session.commit()
        await session.refresh(db_message)
        return db_message

async def get_chat_messages(skip: int = 0, limit: int = 10):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Message).order_by(Message.id.desc()).offset(skip).limit(limit))
        return result.scalars().all()