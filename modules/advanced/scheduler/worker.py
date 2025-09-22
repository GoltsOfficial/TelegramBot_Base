import asyncio
from aiogram import Bot
from Gear.config import config
import datetime

bot = Bot(token=config.BOT_TOKEN)
CHANNEL_ID = -100123456789

async def scheduled_post(text, post_time):
    while True:
        now = datetime.datetime.now()
        if now >= post_time:
            await bot.send_message(CHANNEL_ID, text)
            break
        await asyncio.sleep(30)

async def scheduler():
    # пример расписания
    posts = [
        ("Привет! Сегодняшняя новость.", datetime.datetime(2025, 9, 18, 18, 0)),
        ("Завтра будет акция!", datetime.datetime(2025, 9, 19, 9, 0)),
    ]
    tasks = [scheduled_post(t[0], t[1]) for t in posts]
    await asyncio.gather(*tasks)
