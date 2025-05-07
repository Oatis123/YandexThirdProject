from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Темы")],
        [KeyboardButton(text="💬 Чат с AI")],
        [KeyboardButton(text="ℹ️ Помощь")],
        [KeyboardButton(text="⚙️ Настройки")],
    ],
    resize_keyboard=True
)

main_menu_inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📚 Темы", callback_data="topics")],
        [InlineKeyboardButton(text="💬 Чат с AI", callback_data="chat")],
        [InlineKeyboardButton(text="ℹ️ Помощь", callback_data="help")],
        [InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")],
    ]
)

def get_models_inline_kb(selected: str = None):
    models = [
        ("Qwen 1.5B", "qwen2.5-1.5b"),
        ("GigaChat", "gigachat"),
    ]
    buttons = [
        [InlineKeyboardButton(
            text=("✅ " if selected == code else "") + name,
            callback_data=f"set_model:{code}")]
        for name, code in models
    ]
    buttons.append([InlineKeyboardButton(text="⬅️ В меню", callback_data="back_to_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

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
