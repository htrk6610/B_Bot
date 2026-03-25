import aiohttp
from config import WEATHER_API_KEY


async def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ua"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            if response.status != 200:
                return None

            return {
                "temp": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "city": data["name"]
            }