from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.admins import ADMINS
from database.db import cursor
from aiogram import Bot

router = Router()


@router.message(F.text.startswith("/send"))
async def broadcast(message: Message, bot: Bot):
    if message.from_user.id not in ADMINS:
        return

    text = message.text.replace("/send ", "")

    cursor.execute("SELECT telegram_id FROM users WHERE is_allowed = 1")
    users = cursor.fetchall()

    count = 0

    for user in users:
        try:
            await bot.send_message(user[0], text)
            count += 1
        except:
            pass

    await message.answer(f"✅ Надіслано {count} користувачам")