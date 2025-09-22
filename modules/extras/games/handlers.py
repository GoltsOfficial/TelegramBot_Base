from aiogram import Router, types
from aiogram.filters import Command
from .quiz_data import QUIZ_QUESTIONS
from .utils import generate_quiz_keyboard

router = Router()

# Словарь для отслеживания текущего вопроса пользователя
user_state = {}

@router.message(Command("quiz"))
async def start_quiz(msg: types.Message):
    user_id = msg.from_user.id
    user_state[user_id] = 0
    question = QUIZ_QUESTIONS[0]
    kb = generate_quiz_keyboard(question["options"])
    await msg.answer(question["question"], reply_markup=kb)

@router.callback_query(lambda c: c.data.startswith("quiz:"))
async def handle_answer(call: types.CallbackQuery):
    user_id = call.from_user.id
    selected = call.data.split(":")[1]
    index = user_state.get(user_id, 0)
    question = QUIZ_QUESTIONS[index]

    if selected == question["answer"]:
        await call.message.answer("✅ Правильно!")
    else:
        await call.message.answer(f"❌ Неверно. Правильный ответ: {question['answer']}")

    # следующий вопрос
    index += 1
    if index < len(QUIZ_QUESTIONS):
        user_state[user_id] = index
        next_question = QUIZ_QUESTIONS[index]
        kb = generate_quiz_keyboard(next_question["options"])
        await call.message.answer(next_question["question"], reply_markup=kb)
    else:
        await call.message.answer("🎉 Викторина завершена!")
        user_state.pop(user_id)

    await call.answer()
