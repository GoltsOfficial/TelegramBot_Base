from aiogram import Router, types
from aiogram.filters import Command, Text
from Gear.db import db
from Gear.models import Item  # создаём модель Item в db.py
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
import uuid

router = Router()

@router.inline_query()
async def inline_query_handler(query: types.InlineQuery):
    db.connect()
    items = Item.select().where(Item.title.contains(query.query))[:10]
    db.close()

    results = []
    for i in items:
        results.append(
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title=i.title,
                input_message_content=InputTextMessageContent(
                    f"{i.title} — {i.description}\nЦена: {i.price} ₽"
                )
            )
        )
    await query.answer(results, cache_time=1)
