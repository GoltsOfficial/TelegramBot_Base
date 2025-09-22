from aiogram import Router, types
from aiogram.filters import Command
from .api import ask_alice

router = Router()

@router.message(Command("alice"))
async def start_alice(msg: types.Message):
    await msg.answer("Привет! Напиши сообщение, и Алиса ответит.")

@router.message()
async def handle_alice(msg: types.Message):
    user_text = msg.text
    # Отправляем в Яндекс.Алиса API
    answer = ask_alice(user_text, user_id=msg.from_user.id)
    await msg.answer(answer)
