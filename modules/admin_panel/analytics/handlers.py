from aiogram import Router, types
from Gear.db import db
from Gear.models import EventLog
from aiogram.filters import Command

router = Router()

@router.message(Command("analytics"))
async def cmd_analytics(msg: types.Message):
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Нет доступа")

    db.connect()
    logs = EventLog.select().order_by(EventLog.created_at.desc()).limit(20)
    db.close()

    if not logs:
        return await msg.answer("Событий пока нет.")

    report = ""
    for log in logs:
        report += f"[{log.created_at}] User {log.user_id} — {log.event_type}\n"

    await msg.answer(f"Последние события:\n{report}")
