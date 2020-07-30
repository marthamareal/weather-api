from rest_framework.views import APIView
from rest_framework.response import Response


class WeatherAPIView(APIView):
    """
    """
    def get(self, request):
        articles = [1,2]
        return Response({"articles": articles})