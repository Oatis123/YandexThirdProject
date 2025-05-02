from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_command(msg: Message):
    await msg.answer(
        "/start — Приветствие и краткое объяснение возможностей\n"
        "/topics — Список доступных тем\n"
        "/ask — Задать вопрос AI\n"
        "/chat — Включить свободный чат с AI\n"
        "/help — Памятка по командам"
    )
