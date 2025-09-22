from aiogram import Router, types
from .utils import recognize_voice
import tempfile

router = Router()

@router.message(content_types=types.ContentType.VOICE)
async def voice_to_text(msg: types.Message):
    """
    Принимаем голосовое, сохраняем локально и отправляем в Yandex SpeechKit.
    """
    file_info = await msg.voice.get_file()
    with tempfile.NamedTemporaryFile(suffix=".ogg") as tf:
        await file_info.download(destination=tf.name)
        text = recognize_voice(tf.name)
        await msg.answer(f"Распознанный текст:\n{text}")
