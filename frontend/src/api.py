import aiohttp
import asyncio
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

async def async_fetch_messages():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}/messages/") as response:
            if response.status == 200:
                return await response.json()
            return []

async def async_send_message(content):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{API_URL}/chat/", json={"content": content}) as response:
            if response.status == 200:
                return await response.json()
            return None

def fetch_messages():
    return asyncio.run(async_fetch_messages())

def send_message(content):
    return asyncio.run(async_send_message(content))