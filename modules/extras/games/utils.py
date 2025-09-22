from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_quiz_keyboard(options):
    kb = InlineKeyboardMarkup()
    for opt in options:
        kb.add(InlineKeyboardButton(text=opt, callback_data=f"quiz:{opt}"))
    return kb
