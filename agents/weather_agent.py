import requests
from config import OPENWEATHER_API_KEY

def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url).json()
    return {
        "weather": response["weather"][0]["description"],
        "temperature": response["main"]["temp"]
    }
