from aiogram import Router
from aiogram.types import Message
from bot.ai.gigachat_client import ask_gigachat
from bot.utils.db import async_session, get_user_model
from bot.ai.qwen_client import ask_qwen

router = Router()

def escape_markdown(text: str) -> str:
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return ''.join(f'\\{c}' if c in escape_chars else c for c in text)

@router.message(lambda m: m.text == "Подробнее")
async def details(msg: Message):
    user_prompt = "Объясни подробно для новичка. Не используй markdown, просто текстовое объяснение с примерами кода как в обычном чате>"
    try:
        async with async_session() as session:
            model = await get_user_model(session, msg.from_user.id)
        if model == "gigachat":
            ai_explanation = await ask_gigachat(user_prompt)
        else:
            ai_explanation = await ask_qwen(user_prompt, model)
        ai_explanation = ai_explanation.translate(str.maketrans("", "", "#`*"))
        await msg.answer(f"{escape_markdown(ai_explanation)}", parse_mode='MarkdownV2')
    except Exception as e:
        await msg.answer(f"Ошибка при обращении к AI: {e}")

@router.message(lambda m: m.text == "⬅️ К темам")
async def back_to_topics(msg: Message):
    await msg.answer("Выберите тему:")

@router.message(lambda m: m.text == "⬅️ В меню")
async def back_to_menu(msg: Message):
    await msg.answer("Главное меню:")
