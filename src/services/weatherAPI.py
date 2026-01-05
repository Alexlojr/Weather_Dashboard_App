import os
import requests
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

DEBUG = True

@dataclass
class WeatherData:
    """Weather data structure"""

    city_name: str
    temperature: float
    feels_like: float
    condition: str
    description: str
    humidity: int
    wind_speed: float

    @property
    def temperature_celsius(self) -> int:
        """Converts Kelvin to Celsius"""
        return round(self.temperature - 273.15)

    @property
    def feels_like_celsius(self) -> int:
        return round(self.feels_like - 273.15)


class WeatherService:
    """Weather API data call"""

    def __init__(self,api_key:str):
        self.api_key = api_key
        self.geo_url = 'http://api.openweathermap.org/geo/1.0/direct?'
        self.weather_url = 'https://api.openweathermap.org/data/2.5/weather?'

    def get_geo(self,city:str) -> tuple:
        """Returns city (lat, lon)"""
        url = f"{self.geo_url}?q={city}&limit=1&appid={self.api_key}"
        geo_data = requests.get(url, timeout=10)
        geo_data.raise_for_status()

        data = geo_data.json()
        if not data:
            raise ValueError(f"Cidade '{city}' não encontrada")

        if DEBUG:
            print(data)

        return data[0]['lat'], data[0]['lon']


    def get_weather(self, lat: float, lon: float) -> dict:
        """Returns Weather API data"""
        url = f"{self.weather_url}?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()


    def get_weather_by_city(self, city: str) -> WeatherData:
        """Main function"""
        lat, lon = self.get_geo(city)
        raw_data = self.get_weather(lat, lon)

        # Transforms JSON to API structured data
        return WeatherData(
            city_name=raw_data['name'],
            temperature=raw_data['main']['temp'],
            feels_like=raw_data['main']['feels_like'],
            condition=raw_data['weather'][0]['main'],
            description=raw_data['weather'][0]['description'],
            humidity=raw_data['main']['humidity'],
            wind_speed=raw_data['wind']['speed']
        )




