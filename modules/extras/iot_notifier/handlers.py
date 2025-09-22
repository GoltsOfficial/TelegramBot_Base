from aiogram import Router, types
from aiogram.filters import Command
from config import ALERT_CHAT_ID


router = Router()

@router.message(Command("status"))
async def check_status(msg: types.Message):
    await msg.answer(
        "Модуль IoT уведомлений активен."
        "\nВсе устройства будут присылать сообщения сюда."
    )
