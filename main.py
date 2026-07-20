import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from app.config import BOT_TOKEN
from app.handlers.user import router


bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(router)


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())