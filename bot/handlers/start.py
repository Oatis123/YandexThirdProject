from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards.main import main_menu_kb

router = Router()

@router.message(Command("start"))
async def start(msg: Message):
    await msg.answer(
        f"Привет, {msg.from_user.full_name}!\n\nЯ — ProgHelper AI. Помогу разобраться с программированием, объясню темы, отвечу на вопросы и просто пообщаюсь!",
        reply_markup=main_menu_kb
    )


