from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards.main import topics_kb

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

@router.message(lambda m: m.text == "📚 Темы")
async def topics_menu(msg: Message):
    await msg.answer("Выберите тему:", reply_markup=topics_kb)
