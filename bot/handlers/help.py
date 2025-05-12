from aiogram import Router
from aiogram.types import Message, CallbackQuery
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

@router.callback_query(lambda c: c.data == "help")
async def help_callback(call: CallbackQuery):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_to_menu")]
        ]
    )
    await call.message.edit_text(
        "Доступные функции:\n"
        "- 📚 Темы — изучение основ Python, алгоритмов и структур данных\n"
        "- 💬 Чат с AI — свободное общение с нейросетью по программированию\n"
        "- ⬅️ В меню — возврат в главное меню\n\n"
        "Для возврата в меню используйте кнопку ⬅️ В меню.",
        reply_markup=kb
    )

@router.message(lambda m: m.text == "ℹ️ Помощь")
async def help_keyboard(msg: Message):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_to_menu")]
        ]
    )
    await msg.answer(
        "Доступные функции:\n"
        "- 📚 Темы — изучение основ Python, алгоритмов и структур данных\n"
        "- 💬 Чат с AI — свободное общение с нейросетью по программированию\n"
        "- ⬅️ В меню — возврат в главное меню\n\n"
        "Для возврата в меню используйте кнопку ⬅️ В меню.",
        reply_markup=kb
    )
