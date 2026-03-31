import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage
from database.db import init_db

from handlers import (
    start,
    weather,
    tourism,
    alarm,
    light,
    veterans,
    community,
    complaints,
    fuel,
    corruption,
    admin,
    other,
    back
)

init_db()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

async def main():

    dp.include_router(start.router)
    dp.include_router(weather.router)
    dp.include_router(tourism.router)
    dp.include_router(light.router)
    dp.include_router(community.router)
    dp.include_router(complaints.router)
    dp.include_router(fuel.router)
    dp.include_router(other.router)
    dp.include_router(veterans.router)
    dp.include_router(corruption.router)
    dp.include_router(admin.router)
    dp.include_router(back.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())