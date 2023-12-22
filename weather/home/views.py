from django.shortcuts import render
import requests
import datetime
# Create your views here.
def home(request):
    city = request.GET.get('city','delhi')
    currentdate = datetime.date.today()
    datetimes = datetime.datetime.now()
    time = datetime.time
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&&appid=04d823f6632a163c9510661b4ea23151"
    data = requests.get(url).json()
    payload = {
        'city': data['name'],
        'weather': data['weather'][0]['main'],
        'icon': data['weather'][0]['icon'],
        'kelvin_temperature':data['main']['temp'],
        'calcius_temperature':int(data['main']['temp']-273),
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'],
        'speed': data['wind']['speed'],
        'sunrise_time': data['sys']['sunrise'],
        'sunset_time': data['sys']['sunset'],
        'formatdate':currentdate,
        'time':time 
    }
    context = {'data': payload}
    print(context)
    return render(request, 'home.html', context)
