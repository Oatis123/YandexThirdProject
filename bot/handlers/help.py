from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards.main import main_menu_inline_kb

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

@router.message(lambda m: m.text == "ℹ️ Помощь")
async def help_keyboard(msg: Message):
    await msg.answer(
        "Доступные функции:\n"
        "- 📚 Темы — изучение основ Python, алгоритмов и структур данных\n"
        "- 💬 Чат с AI — свободное общение с нейросетью по программированию\n"
        "- ⬅️ В меню — возврат в главное меню\n\n"
        "Для возврата в меню используйте кнопку ⬅️ В меню.",
        reply_markup=main_menu_inline_kb()
    )
