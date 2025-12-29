import requests

API_KEY = "7b8b7755c75b371f4c27e3e8799bf4e0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_by_city(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    temperature = data["main"]["temp"]

    return map_temperature_to_weather_tag(temperature)


def map_temperature_to_weather_tag(temp):

    if temp >= 30:
        return "hot"
    elif 20 <= temp < 30:
        return "warm"
    elif 10 <= temp < 20:
        return "cool"
    else:
        return "cold"

