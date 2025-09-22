from aiogram import Router, types
from aiogram.filters import Command
from .utils import add_referral
from Gear.db import db
from Gear.models import User

router = Router()


@router.message(Command("referral"))
async def show_referral(msg: types.Message):
    user_id = msg.from_user.id
    db.connect()
    user = User.get_or_none(User.id == user_id)
    if user:
        count = user.referrals.count()
        await msg.answer(f"Вы пригласили {count} пользователей.\nВаш баланс: {user.balance} ₽")
    db.close()


@router.message(Command("invite"))
async def invite_friend(msg: types.Message):
    args = msg.get_args()
    if not args.isdigit():
        return await msg.answer("Используй: /invite <ID_друга>")

    friend_id = int(args)
    add_referral(msg.from_user.id, friend_id, bonus=50)
    await msg.answer(f"Вы пригласили пользователя {friend_id}, бонус 50 ₽ начислен.")
