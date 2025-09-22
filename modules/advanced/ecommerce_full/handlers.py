from aiogram import Router, types
from aiogram.filters import Command
from payments.yookassa import YooKassa
from Gear.db import db
from Gear.models import User, CartItem

router = Router()

@router.message(Command("add"))
async def add_to_cart(msg: types.Message):
    item_id = msg.get_args()
    db.connect()
    user, _ = User.get_or_create(id=msg.from_user.id)
    CartItem.create(user=user, item_id=item_id)
    db.close()
    await msg.answer(f"Товар {item_id} добавлен в корзину.")

@router.message(Command("checkout"))
async def checkout(msg: types.Message):
    db.connect()
    user = User.get_or_none(User.id == msg.from_user.id)
    items = CartItem.select().where(CartItem.user == user)
    total = sum([i.item.price for i in items])
    db.close()

    yk = YooKassa()
    url = yk.create_payment(total, msg.from_user.id, "Оплата корзины")
    await msg.answer(f"Оплатить корзину можно здесь: {url}")
