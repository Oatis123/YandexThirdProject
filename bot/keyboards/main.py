from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_inline_kb():
    return InlineKeyboardMarkup(
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

def get_lessons_keyboard(lessons):
    buttons = [
        [InlineKeyboardButton(text=f"{idx}. {title}", callback_data=f"lesson_{idx}")]
        for idx, title, _ in lessons
    ]
    buttons.append([InlineKeyboardButton(text="⬅️ В меню", callback_data="back_to_menu")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
