from aiogram import Router, types
from aiogram.filters import Command
from extras.voice_to_text.utils import recognize_voice

router = Router()

@router.message(Command("voicelog"))
async def cmd_voicelog(msg: types.Message):
    await msg.answer("Присылайте голосовые, они будут распознаваться и логироваться.")

@router.message(content_types=types.ContentType.VOICE)
async def handle_voice(msg: types.Message):
    file_info = await msg.voice.get_file()
    text = recognize_voice(file_info.file_path)
    await msg.answer(f"Распознанный текст: {text}")
