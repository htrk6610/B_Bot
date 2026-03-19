import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import (
    start,
    weather,
    air,
    alarm,
    power,
    community,
    complaints
)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def main():

    dp.include_router(start.router)
    dp.include_router(weather.router)
    dp.include_router(air.router)
    dp.include_router(alarm.router)
    dp.include_router(power.router)
    dp.include_router(community.router)
    dp.include_router(complaints.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())