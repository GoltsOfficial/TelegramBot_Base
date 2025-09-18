# payments/handlers.py
from aiogram import types, Dispatcher
from payments.yookassa import YooKassa
from Gear.db import db
from Gear.models import User
import asyncio

# Хэндлеры — в функции, чтобы loader мог регистрировать их централизовано
async def cmd_start(msg: types.Message):
    await msg.answer("Привет! Напиши /pay 100 чтобы протестировать оплату.")

async def cmd_pay(msg: types.Message):
    try:
        amount = int(msg.get_args())
    except ValueError:
        await msg.answer("Укажите сумму: /pay 100")
        return

    # создаём или получаем пользователя
    db.connect(reuse_if_open=True)
    user, _ = User.get_or_create(id=msg.from_user.id)
    db.close()

    yk = YooKassa()
    url = yk.create_payment(amount, msg.from_user.id, "Пополнение баланса")
    await msg.answer(f"Оплатить можно здесь:\n{url}")

def register(dp: Dispatcher):
    # если используешь декораторы — лучше регистрировать через dp.message.register
    dp.message.register(cmd_start, commands=["start"])
    dp.message.register(cmd_pay, commands=["pay"])
