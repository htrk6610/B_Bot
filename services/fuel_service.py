import aiohttp
from bs4 import BeautifulSoup

emoji_map = {
    "A-95+": "⛽",
    "А-95": "⛽",
    "А-92": "⛽",
    "ДП": "🚛",
    "Газ": "🔥"
}

URL = "https://index.minfin.com.ua/ua/markets/fuel/reg/kievskaya/"

async def get_fuel_prices():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            html = await response.text()

    soup = BeautifulSoup(html, "html.parser")

    table = soup.find("table")

    if not table:
        return None

    rows = table.find_all("tr")[1:]  # пропускаем заголовок

    result = []

    for row in rows[:5]:  # берем первые 5 строк
        cols = row.find_all("td")

        if len(cols) < 2:
            continue

        fuel_type = cols[0].text.strip()
        price = cols[1].text.strip()

        emoji = emoji_map.get(fuel_type, "⛽, 🚛, 🔥")

        result.append(f"{emoji} {fuel_type} — {price} грн")

    return result