from aiogram import Router, types
from Gear.db import db
from Gear.models import User
from aiogram.filters import Command

router = Router()

@router.message(Command("users"))
async def cmd_users(msg: types.Message):
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Нет доступа")

    db.connect()
    users = User.select()
    db.close()

    text = "Пользователи:\n"
    for u in users:
        text += f"{u.id} | Баланс: {u.balance} ₽ | Подписка: {u.subscription}\n"
    await msg.answer(text)
