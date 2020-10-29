#miscellaneous operations go here!
import requests
import json
import re
import datetime
import wolframalpha
import smtplib
import mysql.connector as sql
from pyowm.owm import OWM  #pip install pyowm
from pyowm.utils import timestamps
import geocoder #pip install geocoder
g = geocoder.ip('me')
#print(g.latlng)
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

#Notes and Reminders
def notrems():
    def notes():
        while True:
            try:
                usr=input("Enter your MySQL Username: ")
                pwd=input("Enter you MySQL Password: ")
                if usr=="":
                    usr="root"
                con=sql.connect(host="localhost",user=usr,password=pwd)
                break
            except:
                print("MySQL Error")
                break
        cur=con.cursor()
        cur.execute("create database if not exists pydeskassist;")
        cur.execute("use pydeskassist;")
        cur.execute("create table if not exists notes(date_added date, note longtext);")
        x1=input("Enter Note: ")
        cur.execute("insert into notes values(curdate(), '%s');"%x1)
        con.commit()
        cur.execute("select * from notes;")
        c=cur.fetchall()
        print(c)
        con.close()

    #notes()

    def reminders():
        while True:
            try:
                usr=input("Enter your MySQL Username: ")
                pwd=input("Enter you MySQL Password: ")
                if usr=="":
                    usr="root"
                con=sql.connect(host="localhost",user=usr,password=pwd)
                break
            except:
                print("MySQL Error")
                break
        cur=con.cursor()
        cur.execute("create database if not exists pydeskassist;")
        cur.execute("use pydeskassist;")
        cur.execute("create table if not exists reminders(date_added date, reminder longtext, date_tbn date, time_tbn time);") #TBN- To Be Notified (OPTIONAL, well yes but actually no)
        x1=input("Enter Reminder: ")
        x2=input("Enter Date to be Notified (YYYY:MM:DD): ")
        x3=input("Enter Time to be Notified (HH:MM:SS): ")
        cur.execute("insert into reminders values(curdate(), '%s', '%s', '%s');"%(x1,x2,x3))
        con.commit()
        cur.execute("select * from reminders;")
        c=cur.fetchall()
        print(c) 
        con.close()

    #reminders()

#notrems()

"""
#Calculations
def Calculations():
    app_id = "Wolframalpha api id" #to be added
    client = wolframalpha.Client(app_id) 
    indx = query.lower().split().index('calculate')  
    query = query.split()[indx + 1:]  
    res = client.query(' '.join(query))  
    answer = next(res.results).text 
    print("The answer is " + answer)  
"""

#Time & Date
def date():
    x = datetime.datetime.now().strftime("%x")  
    print(x)
def time():
    x=datetime.datetime.now().strftime("%H:%M:%S")     
    print(x) 

def year():
    x=datetime.datetime.now()
    print(x.strftime("%Y"))

def month():
    x=datetime.datetime.now()
    print(x.strftime("%B"))

def day():
    x=datetime.datetime.now()
    print(x.strftime("%A"))

#month()
#day()
#year()
#time()
#date()

#Send Emails
"""
def sendEmail(to, content): 
    x=input("Enter your email address: ")
    y=input("Enter email password: ")
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
    server.login(x,y) 
    server.sendmail(x, to, content) 
    server.close() 

try: 
    u=input("What should I say? ")  
    z=input("Enter recepient's email: ") 
    sendEmail(z, u) 
    print("Email has been sent !") 
except Exception as e: 
    print(e) 
    print("I am not able to send this email") 
"""

#Web Search


#Play Offline Songs
