from aiogram import Router, types
from aiogram.filters import Command

router = Router()
SUPPORT_CHAT_ID = -100987654321

@router.message(Command("support"))
async def cmd_support(msg: types.Message):
    await msg.answer("Опишите проблему, и мы свяжемся с вами.")

@router.message()
async def forward_to_support(msg: types.Message):
    await msg.bot.send_message(
        SUPPORT_CHAT_ID,
        f"Сообщение от @{msg.from_user.username or msg.from_user.id}:\n{msg.text}"
    )
