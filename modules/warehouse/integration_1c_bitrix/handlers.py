from aiogram import Router, types
from aiogram.filters import Command
from .api import IntegrationAPI
import os

router = Router()
integration = IntegrationAPI(
    onec_base_url=os.getenv("ONEC_BASE_URL"),
    onec_token=os.getenv("ONEC_TOKEN"),
    bitrix_webhook_url=os.getenv("BITRIX_WEBHOOK")
)

@router.message(Command("sync_orders"))
async def cmd_sync_orders(msg: types.Message):
    integration.sync_data()
    await msg.answer("Данные из 1С синхронизированы в Bitrix24.")
