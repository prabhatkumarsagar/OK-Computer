#miscellaneous operations go here!
import requests
import json
import re
import wikipedia
import datetime
import wolframalpha
import webbrowser
import smtplib
from urllib import request
from bs4 import BeautifulSoup as soup
#import vlc #pip install python-vlc
#from bs4 import BeautifulSoup
#import youtube-dl #RIP
import mysql.connector as sql
from pyowm.owm import OWM  #pip install pyowm
from pyowm.utils import timestamps
import geocoder #pip install geocoder
g = geocoder.ip('me')
#print(g.latlng)
ct=(g.city)
#BeautifulSoup("html.parser")
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
        curr_humidity = y["humidity"]  
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
        x2=input("Enter Date to be Notified (YYYY:MM:DD) (OPTIONAL): ")
        x3=input("Enter Time to be Notified (HH:MM:SS) (OPTIONAL): ")
        if x2=='' and x3=='':
            cur.execute("insert into reminders(date_added,reminder) values(curdate(), '%s');"%x1)
            con.commit()
        else:
            cur.execute("insert into reminders values(curdate(), '%s', '%s', '%s');"%(x1,x2,x3))
            con.commit()
        cur.execute("select * from reminders;")
        c=cur.fetchall()
        print(c) 
        con.close()

    #reminders()

#notrems()

#Calculations
def Calculation():
    url="https://google.com/search?q="
    query=input("Enter Query: ")
    query=query.lower()
    nquery=""
    for i in range(len(query)):
        if query[i]=="+":
            #print("i lob bobs n vagene")
            nquery+=query[i-1]+" "
            nquery+=query[i]
            nquery+=" "+query[i+1]
    nquery=nquery.split()
    print(nquery)
    nurl=url
    for i in nquery:
        if i=='+':
            nurl+='%2B'
            nurl+='%20'
        else:
            nurl+=i
            nurl+='%20'    
    print(nurl)
    try:
        webbrowser.open(nurl)
    except:
        print("Sorry couldn't fetch records, maybe try again later!")

#Calculation()

#Time & Date
def datentime():
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

def sendEmail(): 
    #THIS IS FUCKIN BIBLICAL MATE, IT MIGHT AND MIGHTN'T WORK DEPENDING ON THE FUCKIN EMAIL SERVER AND THE SENDER'S EMAIL SECURITY SO IN SHORT WE NEED AN ALTERNATIVE OR MAYBE WE CAN JUST EXTERMINATE THIS CHARADE ALL THE SAME.
    try:
        sender=input("Enter your email: ")
        sender_pass=input("Enter you email's password: ")
        recipient=input("Enter the recepient's email: ")
        content=input("Enter the content of the email to be sent: ")
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender,sender_pass)
        mail.sendmail(sender,recipient,content)
        mail.close()
        print('Email has been sent successfuly. You can check your inbox.')
    except:
        print("Sorry it looks like i'm having trouble doing that right now, maybe try again later.")
    
"""
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
    z=input(" ") 
    sendEmail(z, u) 
    print("Email has been sent !") 
except Exception as e: 
    print(e) 
    print("I am not able to send this email") 
"""

#sendEmail()

#Play Offline/Online Songs
def playsong():
    def offline():
        print("Alright, fetching your offline music playlist right away!")
        if os.name == "nt":
            music_dir = "C:\\Users\\Local\\Music"
        else:
            music_dir = "HOME$/Music"
        
        songs = os.listdir(music_dir)
        print(songs)
        random = os.startfile(os.path.join(music_dir, songs[1]))
        
    def online():    
        song=input("Alright, what song do you wanna play? ")
        url="https://www.youtube.com/results?search_query="
        url1=song.split()
        for i in url1:
            url+=i
        webbrowser.open(url)
        #LET'S JUST KEEP IT TO THIS FOR NOW! LATER WE CAN MAYBE MAKE A WEBSCRAPER/DRIVER WHICH WILL OPEN THE YOUTUBE PAGE AND AUTOMATICALLY CLICK ON THE FIRST VIDEO AND PLAY IT ALL OF THIS BEING DONE IN BACKGROUND.

#playsong

#Web Search
def web():
    query=input("Enter Web Command(some example of which are \"Open Youtube\" or \"Wikipedia What is Anarchy?\"): ")
    query=query.lower()

    if 'wikipedia' in query:
        try:
            print('Searching Wikipedia...')
            #speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            print("According to Wikipedia")
            print(results)
            #speak(results)
        except:
            print("Please make sure you're entering a valid input!")


    elif 'youtube' in query:
        print("Alright, opening Youtube right away!\n")
        webbrowser.open("youtube.com")

    elif 'google' in query:
        print("Alright, opening Google right away!\n")
        webbrowser.open("google.com")

    elif 'instagram' in query:
        print("Alright, opening Instagram right away!")
        webbrowser.open("instagram.com")
    
    elif 'twitter' in query:
        print("Alright, opening Instagram right away!")
        webbrowser.open("twitter.com")
    
    elif 'reddit' in query:
        print("Alright, opening Instagram right away!")
        webbrowser.open("reddit.com")
    
    elif 'facebook' in query:
        print("Alright, opening Instagram right away!")
        webbrowser.open("facebook.com")

    elif 'search' in query or 'play' in query:
        query = query.replace("search", "")
        query = query.replace("play", "")
        webbrowser.open(query)


    elif "where is" in query:
        query = query.replace("where is", "")
        location = query
        print("You asked to locate",location,"and here you go!")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "")

    elif "news" in query:
        news()
    
    elif "open" in query:
        reg_ex = re.search('open (.+)', query)
        if reg_ex:
            domain = reg_ex.group(1)
            #print(domain)
            url='https://www.'+domain
            #webbrowser.open(url)
            print(url)
            print('The website you have requested has been opened for you.')
        else:
            pass
    else:
        print("LOL it ain't working! maybe try again later bitch!")
web()

def news():
    try:
        news_url="https://news.google.com/news/rss"
        Client=request.urlopen(news_url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        news_list=soup_page.findAll("item")
        for news in news_list[:15]:
            x=news.title.text.encode('utf-8')
            print(x.decode())
    except Exception as e:
            print(e)
            print("Sorry couldn't fetch records, maybe try again later.")
        
#news()


