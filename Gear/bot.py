import asyncio
from aiogram import Bot, Dispatcher
from .config import config
from .logger import setup_logger

logger = setup_logger()

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

async def main():
    logger.info("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
