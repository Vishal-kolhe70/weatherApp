from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Chalisgaon'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e12bfee1b7cb73289f448c29b85baa1f'
    PARAMS = {'units': 'metric'}

    try:
        data = requests.get(url,PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        country = data['sys']['country']
        wind = data['wind']['speed']

        day = datetime.date.today()

        return render(request,'index.html', {'description':description, 'icon':icon, 'temp':temp, 'humidity':humidity, 'wind':wind, 'country':country, 'day':day, 'city':city, 'exception_occured':False})
    except:
        city = 'Chalisgaon'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e12bfee1b7cb73289f448c29b85baa1f'
        PARAMS = {'units': 'metric'}

        data = requests.get(url,PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        day = datetime.date.today
        
        messages.error(request, 'Entered data is not avialable to API')

        return render(request,'index.html', {'description':description, 'icon':icon, 'temp':temp, 'humidity':humidity,'day':day, 'city':city, 'exception_occured':True})
