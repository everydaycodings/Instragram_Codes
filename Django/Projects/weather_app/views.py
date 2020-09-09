import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm
# Create your views here.

def error404(request, exception):
    return render(request, "weather_app/error404.html")

def index(request):

    web = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=b972c56a95dffde980bd98f9980ca3f0"
    
    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    cities = City.objects.all().order_by("-id")
    
    weather_data = []

    for city in cities:
        r = requests.get(web.format(city)).json()

        city_weather = {
            "city": city.city,
            "temperature": r["main"]["temp"],
            "humidity": r["main"]["humidity"],
            "desc": r["weather"][0]["description"],
            "wind_speed": r["wind"]["speed"],
            "icon": r["weather"][0]["icon"],
            "lon": r["coord"]["lon"],
            "lat": r["coord"]["lat"],
        }

        weather_data.append(city_weather)

    context = {"weathers": weather_data, "form": form}
    
    return render(request, "weather_app/index.html", context)