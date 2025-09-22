from aiogram import Router, types
from aiogram.filters import Command
import datetime

router = Router()
ADMIN_ACTIONS_LOG = []  # для примера, лучше в базу

@router.message(Command("adminlog"))
async def cmd_adminlog(msg: types.Message):
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Нет доступа")

    logs = "\n".join([f"{t[0]} | {t[1]}" for t in ADMIN_ACTIONS_LOG])
    await msg.answer(logs or "Логов действий админов пока нет")
