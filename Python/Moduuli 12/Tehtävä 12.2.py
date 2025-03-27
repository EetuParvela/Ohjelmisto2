import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
city = input("Kirjoita kaupungin nimi: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
answer = requests.get(request).json()

print(f"Lämpötila kaupungissa: {city} on {answer["main"]["temp"]:.0f} celsius astetta.")
print(f"Kuvaus: {answer["weather"][0]["description"]}.")