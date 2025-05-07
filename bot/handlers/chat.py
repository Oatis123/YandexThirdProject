from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.ai.gigachat_client import ask_gigachat
from bot.utils.db import async_session, get_user_model
from bot.ai.qwen_client import ask_qwen

router = Router()

class ChatStates(StatesGroup):
    chatting = State()

@router.message(Command("chat"))
async def chat_command(msg: Message, state: FSMContext):
    await msg.answer("Чат-режим с AI активирован! Можете свободно общаться на тему программирования.\nДля выхода напишите /stopchat.")
    await state.set_state(ChatStates.chatting)

@router.message(lambda m: m.text == "💬 Чат с AI")
async def chat_keyboard(msg: Message, state: FSMContext):
    await chat_command(msg, state)

@router.message(Command("stopchat"))
async def stop_chat(msg: Message, state: FSMContext):
    await msg.answer("Чат-режим с AI завершён.")
    await state.clear()

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
