from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.keyboards.main import main_menu_inline_kb, main_menu_reply_kb, get_models_inline_kb
from bot.utils.db import async_session, get_user_model, set_user_model, ensure_user_exists
from sqlalchemy.ext.asyncio import AsyncSession

router = Router()

@router.message(F.text == "⚙️ Настройки")
async def settings_menu(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    async with async_session() as session:
        model = await get_user_model(session, user_id)
    await msg.answer(
        f"Настройки\n\nТекущая модель: <b>{model}</b>\n\nВыберите модель для общения:",
        reply_markup=get_models_inline_kb(selected=model),
        parse_mode="HTML"
    )

@router.callback_query(F.data == "settings")
async def settings_callback(call: CallbackQuery):
    user_id = call.from_user.id
    async with async_session() as session:
        model = await get_user_model(session, user_id)
    await call.message.edit_text(
        f"Настройки\n\nТекущая модель: <b>{model}</b>\n\nВыберите модель для общения:",
        reply_markup=get_models_inline_kb(selected=model),
        parse_mode="HTML"
    )

@router.callback_query(F.data.startswith("set_model:"))
async def set_model_callback(call: CallbackQuery):
    user_id = call.from_user.id
    model = call.data.split(":", 1)[1]
    async with async_session() as session:
        await ensure_user_exists(session, user_id, call.from_user.username)
        await set_user_model(session, user_id, model)
    await call.answer(f"Модель изменена на {model}", show_alert=True)
    await call.message.edit_text(
        f"Настройки\n\nТекущая модель: <b>{model}</b>\n\nВыберите модель для общения:",
        reply_markup=get_models_inline_kb(selected=model),
        parse_mode="HTML"
    )

@router.callback_query(F.data == "back_to_menu")
async def back_to_menu_callback(call: CallbackQuery):
    await call.message.edit_text(
        "Главное меню:",
        reply_markup=main_menu_inline_kb()
    )

@router.message(F.text == "⬅️ В меню")
async def back_to_menu_reply(msg: Message, state: FSMContext):
    await msg.answer(
        "Главное меню:",
        reply_markup=main_menu_reply_kb()
    )