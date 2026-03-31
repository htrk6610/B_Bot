# utils/broadcast.py
async def send_to_all(bot, cursor, text):
    cursor.execute("SELECT telegram_id FROM users WHERE is_allowed = 1")
    users = cursor.fetchall()

    for user in users:
        try:
            await bot.send_message(user[0], text)
        except:
            pass