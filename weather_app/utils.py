import requests
from weather_api import settings


class OpenWeather():

    def get_api_data(self, city, period):
        session = requests.Session()
        session.headers.update(
            {
                'Content-Type': 'application/json'
            }
        )
        if period:
            url = 'http://pro.openweathermap.org/data/2.5/forecast/{}'.format(period)
        else:
            url = 'http://api.openweathermap.org/data/2.5/weather'

        response = session.get(url, params={'q': city, 'appid': settings.WEATHER_API_KEY})
        return response.json()
