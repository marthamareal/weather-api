from django.urls import path

from weather_app.views import WeatherAPIView

urlpatterns = [
    path('temperature/', WeatherAPIView.as_view()),
    ]