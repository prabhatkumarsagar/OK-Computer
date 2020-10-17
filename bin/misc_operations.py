#miscellaneous operations go here!
import requests
import json
import re
from pyowm.owm import OWM  #pip install pyowm
from pyowm.utils import timestamps
import geocoder #pip install geocoder
g = geocoder.ip('me')
print(g.latlng)
ct=(g.city)

#weather
def weather_curr(city): #to be replaced with - elif 'weather' in command:    
    #api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}          
    api_key = "cd140d1c1404cba5de2dabf6bcd00f52" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "&q=" + city + "&appid=" + api_key
    response = requests.get(url)  
    x = response.json()  
    if x["cod"] == "404":  
        print("Oops! it looks like i ran into a problem fetching your request, maybe try again later?")
    else:
        y = x["main"]  
        curr_temperature = y["temp"]  
        curr_pressure = y["pressure"]  
        curr_humidiy = y["humidity"]  
        z = x["weather"]  
        weather_desc = z[0]["description"]  
        print("The current temperatre in %s (in Celcius Scale) is " % city +str(round(curr_temperature-273))+" degree celsius" +". It's a " +str(weather_desc))  

#weather_curr(ct)


#weather forecaster
def weather_forec(city):
    owm = OWM('cd140d1c1404cba5de2dabf6bcd00f52')
    mgr=owm.weather_manager()
    loc = mgr.weather_at_place(city)
    weather = loc.weather
    temp = weather.temperature(unit='celsius')
    #for key,val in temp.items():
    #    print(f'{key} => {val}')
    loa = mgr.forecast_at_place(city,'3h')
    tomorrow=timestamps.tomorrow()
    forecasttt=loa.get_weather_at(tomorrow)
    print(forecasttt)

#weather_forec(ct)

"""
###other method
lat=str(g.lat)
lon=str(g.lng)
bs_url="https://api.openweathermap.org/data/2.5/onecall?lat="+lat+"&lon="+lon+"&exclude=hourly,daily&appid=cd140d1c1404cba5de2dabf6bcd00f52"

response = requests.get(bs_url)  
x = response.json()  
print(x)
"""

#Emails
