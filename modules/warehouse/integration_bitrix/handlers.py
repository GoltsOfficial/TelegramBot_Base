from aiogram import Router, types
from aiogram.filters import Command
from .api import Bitrix24API
import os

router = Router()
bitrix = Bitrix24API(webhook_url=os.getenv("BITRIX_WEBHOOK"))

@router.message(Command("bitrix_deals"))
async def cmd_bitrix_deals(msg: types.Message):
    deals = bitrix.call_method("crm.deal.list")
    if "result" not in deals or not deals["result"]:
        await msg.answer("Нет сделок в Bitrix24.")
        return
    report = "\n".join([f"Deal {d['ID']}: {d['TITLE']}" for d in deals["result"]])
    await msg.answer(f"Сделки из Bitrix24:\n{report}")
