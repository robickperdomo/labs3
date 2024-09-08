import requests
import json

API_KEY = 'f3826914fe6834d20bbf17da42987559'
CITY = 'SALVADOR'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(api_key, city):
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'es'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        print(json.dumps(weather_data, indent=4, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")

if __name__ == '__main__':
    get_weather(API_KEY, CITY)