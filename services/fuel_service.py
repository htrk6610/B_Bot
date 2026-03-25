import aiohttp
from bs4 import BeautifulSoup


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

    for row in rows[:5]:  # берем топ 5 (чтобы не спамить)
        cols = row.find_all("td")

        if len(cols) < 2:
            continue

        fuel_type = cols[0].text.strip()
        price = cols[1].text.strip()

        result.append(f"{fuel_type}: {price} грн")

    return result