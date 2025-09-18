import asyncio
from aiogram import Bot, Dispatcher, types
from Gear.config import config
from payments.yookassa import YooKassa
from Gear.db import db
from Gear.models import User


bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


# Создаём таблицы
db.connect()
db.create_tables([User], safe=True)
db.close()

@dp.message(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Привет! Напиши /pay 100 чтобы протестировать оплату.")

@dp.message(commands=["pay"])
async def pay(msg: types.Message):
    try:
        amount = int(msg.get_args())
    except ValueError:
        return await msg.answer("Укажите сумму: /pay 100")

    # создаём или получаем пользователя
    db.connect()
    user, _ = User.get_or_create(id=msg.from_user.id)
    db.close()

    yk = YooKassa()
    url = yk.create_payment(amount, msg.from_user.id, "Пополнение баланса")
    await msg.answer(f"Оплатить можно здесь:\n{url}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
