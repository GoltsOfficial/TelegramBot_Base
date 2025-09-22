from aiogram import Router, types
from aiogram.filters import Command
from Gear.db import db
from Gear.models import User

router = Router()

# Укажи ID админа
ADMIN_ID = 123456789

@router.message(Command("broadcast"))
async def cmd_broadcast(msg: types.Message):
    # Проверка прав
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Нет доступа")

    text = msg.get_args()
    if not text:
        return await msg.answer("Используй: /broadcast текст_сообщения")

    # Выборка всех пользователей
    db.connect()
    users = User.select(User.id)
    db.close()

    count = 0
    for u in users:
        try:
            await msg.bot.send_message(u.id, text)
            count += 1
        except Exception:
            pass

    await msg.answer(f"Рассылка завершена. Доставлено {count} сообщений.")
