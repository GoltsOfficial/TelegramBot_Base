import asyncio
import feedparser
from aiogram import Bot
from Gear.config import config

bot = Bot(token=config.BOT_TOKEN)
CHANNEL_ID = -100123456789  # id канала

async def publish_feed():
    url = "https://example.com/rss"
    feed = feedparser.parse(url)

    for entry in feed.entries[:5]:  # последние 5 постов
        text = f"{entry.title}\n{entry.link}"
        await bot.send_message(CHANNEL_ID, text)

async def scheduler():
    while True:
        await publish_feed()
        await asyncio.sleep(3600)  # каждый час
