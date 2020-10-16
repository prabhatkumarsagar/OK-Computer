
import requests
import json
import re
import pyowm
import geocoder #pip install geocoder
g = geocoder.ip('me')
print(g.latlng)
ct=(g.city)

#weather/weather forecast
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

"""

### to be continued (weather forecaster)s
def weather_forec():
import pyowm

owm = pyowm.OWM(
    'cd140d1c1404cba5de2dabf6bcd00f52')

city = 'Lisbon'

loc = owm.weather_at_place(city)
weather = loc.get_weather()

# temperature
temp = weather.get_temperature(unit='celsius')

for key,val in temp.items():
    print(f'{key} => {val}')

# humidity, wind, rain, snow
humidity = weather.get_humidity()
wind = weather.get_wind()
rain = weather.get_rain()
snow = weather.get_snow()

print(f'humidity = {humidity}')
print(f'wind = {wind}')
print(f'rain = {rain}')
print(f'snow = {snow}')

# sun rise and sun set
sr = weather.get_sunrise_time(timeformat='iso')
ss = weather.get_sunset_time(timeformat='iso')
print(f'SunRise = {sr}') 
print(f'SunSet = {ss}')

# clouds and rain
loc = owm.three_hours_forecast(city)
print(loc)
clouds = str(loc.will_have_clouds())
rain = str(loc.will_have_rain())

print('will have clouds? ' + clouds)
print('will have rain? ' + rain)
"""