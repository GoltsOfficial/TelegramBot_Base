# Gear/payments/webhook.py
from aiogram import types
from Gear.payments.yookassa import YooKassa

async def process_payment_notification(request: types.Request):
    notification = await request.json()
    payment_id = notification.get("object", {}).get("id")
    status = notification.get("object", {}).get("status")
    # Обработка уведомления о платеже
