from rest_framework.views import APIView
from rest_framework.response import Response

from weather_app.utils import OpenWeather


class WeatherAPIView(APIView):
    """
    """
    period = ['hourly', 'daily']

    def post(self, request):
        period = request.query_params.get('period')
        city = request.query_params.get('city')
        weather = OpenWeather()
        data = weather.get_api_data(city, period)
        return Response(data)

