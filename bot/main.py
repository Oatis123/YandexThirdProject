from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.types import Message
from dotenv import load_dotenv
import asyncio
import os
import logging
from bot.utils.db import init_db
from bot.handlers.start import router as start_router
from bot.handlers.topics import router as topics_router
from bot.handlers.topic_details import router as topic_details_router
from bot.handlers.ask import router as ask_router
from bot.handlers.chat import router as chat_router
from bot.handlers.help import router as help_router
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