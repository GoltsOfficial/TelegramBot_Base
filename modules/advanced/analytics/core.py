# modules/advanced/analytics/core.py
from aiogram import Router, types
from Gear.db import db
from Gear.models import EventLog
from aiogram.filters import Command
import datetime

router = Router()

# Модель EventLog (если еще нет)
# class EventLog(Model):
#     user_id = IntegerField()
#     event_type = CharField()
#     details = TextField(null=True)
#     created_at = DateTimeField(default=datetime.datetime.now)

# Запись события
async def log_event(user_id: int, event_type: str, details: str = None):
    db.connect()
    EventLog.create(
        user_id=user_id,
        event_type=event_type,
        details=details
    )
    db.close()

# Команда для получения отчёта по последним событиям
@router.message(Command("analytics"))
async def cmd_analytics(msg: types.Message):
    # Проверка на админа (можно вынести в env)
    ADMIN_ID = 123456789
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Нет доступа")

    db.connect()
    logs = EventLog.select().order_by(EventLog.created_at.desc()).limit(20)
    db.close()

    if not logs:
        return await msg.answer("Событий пока нет.")

    report = ""
    for log in logs:
        report += f"[{log.created_at.strftime('%Y-%m-%d %H:%M:%S')}] User {log.user_id} — {log.event_type}\n"

    await msg.answer(f"Последние события:\n{report}")
