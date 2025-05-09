import os
from aiogram import Router
from aiogram.types import Message, CallbackQuery
from bot.keyboards.main import main_menu_inline_kb, get_lessons_keyboard
from aiogram.utils.markdown import hbold

router = Router()

COURSE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'python_course')

def get_lessons():
    files = sorted(os.listdir(COURSE_PATH))
    lessons = []
    for idx, filename in enumerate(files, 1):
        if filename.endswith('.txt'):
            title = filename.split('_', 1)[-1].replace('.txt', '').replace('_', ' ')
            lessons.append((idx, title, filename))
    return lessons

@router.message(lambda m: m.text == "📚 Темы")
async def show_topics(msg: Message):
    lessons = get_lessons()
    text = hbold("Темы Python курса:") + "\n\n" + "\n".join([f"{idx}. {title}" for idx, title, _ in lessons])
    await msg.answer(text, reply_markup=get_lessons_keyboard(lessons), parse_mode="HTML")

@router.callback_query(lambda c: c.data == "topics")
async def topics_callback(call: CallbackQuery):
    lessons = get_lessons()
    text = hbold("Темы Python курса:") + "\n\n" + "\n".join([f"{idx}. {title}" for idx, title, _ in lessons])
    await call.message.edit_text(text, reply_markup=get_lessons_keyboard(lessons), parse_mode="HTML")

@router.callback_query(lambda c: c.data.startswith("lesson_") and not c.data.startswith("lesson_ai_"))
async def lesson_callback(call: CallbackQuery):
    lesson_idx = int(call.data.split("_")[1])
    lessons = get_lessons()
    if 1 <= lesson_idx <= len(lessons):
        _, title, filename = lessons[lesson_idx - 1]
        with open(os.path.join(COURSE_PATH, filename), encoding="utf-8") as f:
            content = f.read()
        from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
        kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Подробнее", callback_data=f"lesson_ai_{lesson_idx}")],
                [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_to_menu")]
            ]
        )
        await call.message.edit_text(
            f"<b>{lesson_idx}. {title}</b>\n\n{content}",
            reply_markup=kb,
            parse_mode="HTML"
        )
    else:
        await call.answer("Урок не найден", show_alert=True)

@router.callback_query(lambda c: c.data.startswith("lesson_ai_"))
async def lesson_ai_callback(call: CallbackQuery):
    lesson_idx = int(call.data.split("_")[2])
    lessons = get_lessons()
    if 1 <= lesson_idx <= len(lessons):
        _, title, filename = lessons[lesson_idx - 1]
        with open(os.path.join(COURSE_PATH, filename), encoding="utf-8") as f:
            content = f.read()
        from bot.utils.db import async_session, get_user_model
        from bot.ai.gigachat_client import ask_gigachat
        from bot.ai.qwen_client import ask_qwen
        user_id = call.from_user.id
        async with async_session() as session:
            model = await get_user_model(session, user_id)
        prompt = f"Объясни подробно для новичка: {content}. Не используй markdown, просто текстовое объяснение с примерами кода как в обычном чате."
        if model == "gigachat":
            ai_text = await ask_gigachat(prompt)
        else:
            ai_text = await ask_qwen(prompt, model)
        from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
        kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_to_menu")]
            ]
        )
        await call.message.edit_text(
            f"<b>{lesson_idx}. {title} — AI объяснение</b>\n\n{ai_text}",
            reply_markup=kb,
            parse_mode="HTML"
        )
    else:
        await call.answer("Урок не найден", show_alert=True)

@router.callback_query(lambda c: c.data == "back_to_menu")
async def back_to_menu(call: CallbackQuery):
    await call.message.edit_text("Главное меню:", reply_markup=main_menu_inline_kb())
