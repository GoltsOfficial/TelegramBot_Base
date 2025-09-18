from yookassa import Configuration, Payment
from Gear.config import config

class YooKassa:
    def __init__(self):
        Configuration.account_id = config.YK_ACCOUNT_ID
        Configuration.secret_key = config.YK_SECRET_KEY

    def create_payment(self, amount: int, user_id: int, description: str):
        payment = Payment.create({
            "amount": {
                "value": str(amount),
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://t.me/YourBot"
            },
            "capture": True,
            "description": description,
            "metadata": {"user_id": str(user_id)}
        })
        return payment.confirmation.confirmation_url
