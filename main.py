from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from Gear.config import config

# модуль payments
from payments.yookassa import YooKassa

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Привет! Напиши /pay 100 чтобы протестировать оплату")

@dp.message_handler(commands=["pay"])
async def pay(msg: types.Message):
    try:
        amount = int(msg.get_args())
    except ValueError:
        return await msg.answer("Укажи сумму: /pay 100")

    yk = YooKassa()
    url = yk.create_payment(amount, "Пополнение баланса")
    await msg.answer(f"Оплатить можно тут:\n{url}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
