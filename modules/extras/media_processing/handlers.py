from aiogram import Router, types
from aiogram.filters import Command
from .processing import resize_image, add_watermark, convert_video
import os

router = Router()

MEDIA_DIR = "temp_media"

os.makedirs(MEDIA_DIR, exist_ok=True)

@router.message(Command("resize"))
async def cmd_resize(msg: types.Message):
    if not msg.photo:
        return await msg.answer("Пришлите фото.")
    photo = msg.photo[-1]
    file_path = f"{MEDIA_DIR}/{photo.file_id}.jpg"
    await photo.download(destination=file_path)
    output = f"{MEDIA_DIR}/resized_{photo.file_id}.jpg"
    resize_image(file_path, output)
    await msg.answer_photo(types.InputFile(output))

@router.message(Command("watermark"))
async def cmd_watermark(msg: types.Message):
    if not msg.photo:
        return await msg.answer("Пришлите фото.")
    photo = msg.photo[-1]
    file_path = f"{MEDIA_DIR}/{photo.file_id}.jpg"
    await photo.download(destination=file_path)
    output = f"{MEDIA_DIR}/wm_{photo.file_id}.jpg"
    add_watermark(file_path, output)
    await msg.answer_photo(types.InputFile(output))

@router.message(Command("convert_video"))
async def cmd_convert_video(msg: types.Message):
    if not msg.video:
        return await msg.answer("Пришлите видео.")
    video = msg.video
    file_path = f"{MEDIA_DIR}/{video.file_id}.mp4"
    await video.download(destination=file_path)
    output = f"{MEDIA_DIR}/conv_{video.file_id}.mp4"
    convert_video(file_path, output)
    await msg.answer_video(types.InputFile(output))
