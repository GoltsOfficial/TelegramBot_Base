from aiogram import Router, types
from aiogram.filters import Command
import gspread
import os
from dotenv import load_dotenv

load_dotenv()
router = Router()

gc = gspread.service_account(filename=os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))
sheet = gc.open_by_key(os.getenv("GOOGLE_SHEET_KEY")).sheet1


@router.message(Command("lead"))
async def collect_lead(msg: types.Message):
    await msg.answer("Введите email для связи:")


@router.message()
async def save_lead(msg: types.Message):
    email = msg.text
    sheet.append_row([email])
    await msg.answer(f"Email {email} сохранён в CRM.")
