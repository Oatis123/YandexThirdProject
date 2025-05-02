from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.types import Message
from dotenv import load_dotenv
import asyncio
import os
import logging
from utils.db import init_db
from handlers.start import router as start_router
from handlers.topics import router as topics_router
from handlers.topic_details import router as topic_details_router
from handlers.ask import router as ask_router
from handlers.chat import router as chat_router
from handlers.help import router as help_router
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def main():
    logging.basicConfig(level=logging.INFO)
    await init_db()
    bot = Bot(token=TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(start_router)
    dp.include_router(topics_router)
    dp.include_router(topic_details_router)
    dp.include_router(ask_router)
    dp.include_router(chat_router)
    dp.include_router(help_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())