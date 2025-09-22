from aiogram import Router, types
from aiogram.filters import Command
import gspread
import os
from dotenv import load_dotenv

load_dotenv()

router = Router()

# Настройка Google Sheets
gc = gspread.service_account(filename=os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON"))
sheet = gc.open_by_key(os.getenv("GOOGLE_SHEET_KEY")).sheet1  # Берём первый лист

@router.message(Command("lead"))
async def cmd_lead(msg: types.Message):
    await msg.answer("Введите ваш email для связи:")

@router.message()
async def collect_lead(msg: types.Message):
    email = msg.text
    sheet.append_row([email])  # Добавляем в таблицу
    await msg.answer(f"Спасибо! Ваш email сохранён: {email}")
