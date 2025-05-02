from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
from aiogram.utils.markdown import hcode
from bot.ai.gigachat_client import ask_gigachat

router = Router()

class AskStates(StatesGroup):
    waiting_for_question = State()

@router.message(Command("ask"))
async def ask_command(msg: Message, state: FSMContext):
    await msg.answer("Пожалуйста, напишите свой вопрос по программированию. Я постараюсь ответить с помощью AI.")
    await state.set_state(AskStates.waiting_for_question)

@router.message(AskStates.waiting_for_question)
async def process_question(msg: Message, state: FSMContext):
    await msg.answer("Генерирую ответ AI, пожалуйста, подождите...")
    try:
        answer = await ask_gigachat(msg.text)
        await msg.answer(hcode(answer))
    except Exception as e:
        await msg.answer(f"Ошибка при обращении к AI: {e}")
    await state.clear()
