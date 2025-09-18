from aiogram import Bot
from Gear.config import config
from Gear.db import db
from Gear.models import User
import asyncio

bot = Bot(token=config.BOT_TOKEN)

async def process_payment_notification(request):
    data = await request.json()
    payment_id = data.get("object", {}).get("id")
    status = data.get("object", {}).get("status")
    amount = data.get("object", {}).get("amount", {}).get("value")
    user_id = data.get("object", {}).get("metadata", {}).get("user_id")

    if status == "succeeded" and user_id:
        with db.atomic():
            user = User.get_or_none(User.id == int(user_id))
            if user:
                user.balance += float(amount)
                user.save()

        asyncio.run(bot.send_message(user_id, f"Баланс пополнен на {amount} ₽!"))
