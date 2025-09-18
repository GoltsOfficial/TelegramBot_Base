# Gear/payments/yookassa.py
from yookassa_api import YooKassa, PaymentAmount, Confirmation
from yookassa_api.types import CurrencyType, ConfirmationType
from Gear.config import config

class YooKassa:
    def __init__(self):
        self.client = YooKassa(
            config.YK_SECRET_KEY,
            shop_id=config.YK_ACCOUNT_ID
        )

    def create_payment(self, amount: int, description: str):
        payment = self.client.create_payment(
            PaymentAmount(value=amount, currency=CurrencyType.RUB),
            description=description,
            confirmation=Confirmation(
                type=ConfirmationType.REDIRECT,
                return_url="https://t.me/YourBot"
            )
        )
        return payment.confirmation.confirmation_url
