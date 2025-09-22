from aiogram import Router, types
from Gear.db import db
from Gear.models import User, CartItem
from aiogram.filters import Command

router = Router()

@router.message(Command("orders"))
async def cmd_orders(msg: types.Message):
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Нет доступа")

    db.connect()
    users = User.select()
    report = ""
    for user in users:
        items = CartItem.select().where(CartItem.user == user)
        if items:
            report += f"User {user.id}:\n"
            for i in items:
                report += f" - {i.item_id} ({i.item.price} ₽)\n"
    db.close()
    await msg.answer(report or "Заказов нет")
