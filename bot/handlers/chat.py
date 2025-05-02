from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.markdown import hcode
from bot.ai.gigachat_client import ask_gigachat

router = Router()

class ChatStates(StatesGroup):
    chatting = State()

@router.message(Command("chat"))
async def chat_command(msg: Message, state: FSMContext):
    await msg.answer("Чат-режим с AI активирован! Можете свободно общаться на тему программирования.\nДля выхода напишите /stopchat.")
    await state.set_state(ChatStates.chatting)

@router.message(Command("stopchat"))
async def stop_chat(msg: Message, state: FSMContext):
    await msg.answer("Чат-режим с AI завершён.")
    await state.clear()

@router.message(ChatStates.chatting)
async def chat_with_ai(msg: Message, state: FSMContext):
    await msg.answer("AI думает...")
    try:
        answer = await ask_gigachat(msg.text)
        await msg.answer(hcode(answer))
    except Exception as e:
        await msg.answer(f"Ошибка при обращении к AI: {e}")
