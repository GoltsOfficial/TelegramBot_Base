from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from Gear.config import config
from payments.yookassa import YooKassa
from Gear.db import db
from models import User

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

# Инициализация базы (создание таблиц)
db.connect()
db.create_tables([User], safe=True)
db.close()

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Привет! Напиши /pay 100 чтобы протестировать оплату.")

@dp.message_handler(commands=["pay"])
async def pay(msg: types.Message):
    try:
        amount = int(msg.get_args())
    except ValueError:
        return await msg.answer("Укажите сумму: /pay 100")

    # создаем или получаем пользователя
    db.connect()
    user, _ = User.get_or_create(id=msg.from_user.id)
    db.close()

    yk = YooKassa()
    url = yk.create_payment(amount, msg.from_user.id, "Пополнение баланса")
    await msg.answer(f"Оплатить можно здесь:\n{url}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
