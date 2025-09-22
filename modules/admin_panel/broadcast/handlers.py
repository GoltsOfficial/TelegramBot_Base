from aiogram import Router, types
from Gear.db import db
from Gear.models import User
from aiogram.filters import Command

router = Router()

@router.message(Command("broadcast"))
async def cmd_broadcast(msg: types.Message):
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Нет доступа")

    text = msg.get_args()
    if not text:
        return await msg.answer("Используй: /broadcast текст_сообщения")

    db.connect()
    users = User.select()
    db.close()

    count = 0
    for u in users:
        try:
            await msg.bot.send_message(u.id, text)
            count += 1
        except Exception:
            pass

    await msg.answer(f"Рассылка завершена. Доставлено {count} сообщений.")
