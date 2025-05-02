from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

TOPICS = [
    "Основы Python",
    "Основы алгоритмов",
    "Основы структуры данных"
]

@router.message(Command("topics"))
async def topics(msg: Message):
    text = "\n".join(f"{i+1}. {t}" for i, t in enumerate(TOPICS))
    await msg.answer(f"Доступные темы:\n{text}\n\nВыберите номер темы для подробностей.")
