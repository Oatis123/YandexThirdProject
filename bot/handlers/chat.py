from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.keyboards.main import main_menu_inline_kb, main_menu_reply_kb
from bot.ai.gigachat_client import ask_gigachat
from bot.utils.db import async_session, get_user_model
from bot.ai.qwen_client import ask_qwen

router = Router()

class ChatStates(StatesGroup):
    chatting = State()

@router.message(Command("chat"))
async def chat_command(msg: Message, state: FSMContext):
    await msg.answer(
        "Чат-режим с AI активирован! Можете свободно общаться на тему программирования.\nДля выхода напишите /stopchat.",
        reply_markup=main_menu_reply_kb()
    )
    await state.set_state(ChatStates.chatting)

@router.callback_query(lambda c: c.data == "chat")
async def chat_callback(call: CallbackQuery, state: FSMContext):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="/stopchat", callback_data="stopchat_auto")]
        ]
    )
    await call.message.edit_text(
        "Чат-режим с AI активирован! Можете свободно общаться на тему программирования.\nДля выхода нажмите кнопку ниже или напишите /stopchat.",
        reply_markup=kb
    )
    await state.set_state(ChatStates.chatting)

@router.callback_query(lambda c: c.data == "stopchat_auto")
async def stopchat_auto_callback(call: CallbackQuery, state: FSMContext):
    await stop_chat(call.message, state)

@router.message(lambda m: m.text == "💬 Чат с AI")
async def chat_keyboard(msg: Message, state: FSMContext):
    await chat_command(msg, state)

@router.message(Command("stopchat"))
async def stop_chat(msg: Message, state: FSMContext):
    await msg.answer(
        "Чат-режим с AI завершён.",
        reply_markup=main_menu_reply_kb()
    )
    await state.clear()

@router.message(lambda m: m.text == "⬅️ В меню")
async def back_to_menu_reply(msg: Message, state: FSMContext):
    await msg.answer(
        "Главное меню:",
        reply_markup=main_menu_inline_kb()
    )

@router.message(ChatStates.chatting)
async def chat_with_ai(msg: Message, state: FSMContext):
    await msg.answer("AI думает...")
    try:
        async with async_session() as session:
            model = await get_user_model(session, msg.from_user.id)
        if model == "gigachat":
            answer = await ask_gigachat(msg.text)
        else:
            answer = await ask_qwen(msg.text, model)
        await msg.answer(answer)
    except Exception as e:
        await msg.answer(f"Ошибка при обращении к AI: {e}")
