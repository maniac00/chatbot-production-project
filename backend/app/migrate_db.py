import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
from app.models import Base

load_dotenv()
ASYNC_DB_URL = os.getenv("DATABASE_URL").replace("postgresql://", "postgresql+asyncpg://")

async def reset_database():
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def main():
    await reset_database()

if __name__ == "__main__":
    asyncio.run(main())