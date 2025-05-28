from django.shortcuts import render
from django.urls import reverse
from .forms import *
import requests
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    EWFO=WeatherForm()
    submitted=False
    d={'EWFO':EWFO,'submitted':submitted }


    if request.method=='POST':
        city_name=request.POST['city']
        print(city_name)
        api_key='ee8c7a6385fee7e7bfb770731507c9f6'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        response = requests.get(url)
        weather_data=response.json()
        print(weather_data)
        submitted=True
        humidity=weather_data['main']['humidity']
        temperature=weather_data['main']['temp']
        max_temp=weather_data['main']['temp_max']
        wind_speed=weather_data['wind']['speed']


        d={
            'EWFO':EWFO,
            'submitted':submitted,
            'city_name':city_name,
            'humidity':humidity,
            'temperature':temperature,
            'max_temp':max_temp,
            'wind_speed':wind_speed
        }



        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
        else:
                ip = request.META.get('REMOTE_ADDR')
            
        print(f"User IP address is: {ip}")
        return render(request,'home.html',d)
    return render(request,'home.html',d)