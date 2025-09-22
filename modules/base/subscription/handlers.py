from aiogram import Router, types
from aiogram.filters import Command
from payments.yookassa import YooKassa
from Gear.db import db
from Gear.models import User
from dotenv import load_dotenv
import os

load_dotenv()

router = Router()

@router.message(Command("subscribe"))
async def cmd_subscribe(msg: types.Message):
    db.connect()
    user, _ = User.get_or_create(id=msg.from_user.id)
    db.close()

    yk = YooKassa()
    # Сумма подписки можно тоже вынести в env
    price = int(os.getenv("SUBSCRIPTION_PRICE", 199))
    url = yk.create_payment(price, msg.from_user.id, "Подписка на месяц")
    await msg.answer(f"Оплатить подписку: {url}")
