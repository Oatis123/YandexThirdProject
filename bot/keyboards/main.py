from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Темы")],
        [KeyboardButton(text="💬 Чат с AI")],
        [KeyboardButton(text="ℹ️ Помощь")]
    ],
    resize_keyboard=True
)

topics_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1. Основы Python")],
        [KeyboardButton(text="2. Основы алгоритмов")],
        [KeyboardButton(text="3. Основы структуры данных")],
        [KeyboardButton(text="⬅️ В меню")]
    ],
    resize_keyboard=True
)

details_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Подробнее")],
        [KeyboardButton(text="⬅️ К темам")]
    ],
    resize_keyboard=True
)
