from aiogram import Router, types
from Gear.db import db
from Gear.models import User
from extras.referral.utils import add_referral
from aiogram.filters import Command

router = Router()

@router.message(Command("referrals"))
async def show_referrals(msg: types.Message):
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Нет доступа")

    db.connect()
    users = User.select()
    report = ""
    for u in users:
        report += f"{u.id} | Пригласил: {u.referrals.count()} | Баланс: {u.balance} ₽\n"
    db.close()
    await msg.answer(report)
