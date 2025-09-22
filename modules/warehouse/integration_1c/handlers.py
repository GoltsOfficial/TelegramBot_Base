from aiogram import Router, types
from aiogram.filters import Command
from .api import OneCAPI
import os

router = Router()
onec = OneCAPI(base_url=os.getenv("ONEC_BASE_URL"), token=os.getenv("ONEC_TOKEN"))

@router.message(Command("1c_orders"))
async def cmd_1c_orders(msg: types.Message):
    orders = onec.get_data("orders")
    if not orders:
        await msg.answer("Нет заказов в 1С.")
        return
    report = "\n".join([f"Order {o['id']}: {o['total']} ₽" for o in orders])
    await msg.answer(f"Заказы из 1С:\n{report}")
