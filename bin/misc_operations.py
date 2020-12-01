#miscellaneous operations go here!
import requests
import json
import os
import re
import wikipedia
import datetime
import wolframalpha
import webbrowser
import smtplib

try:
    from bin import mailer
    from bin import voice_io
    from bin import wolfy
    from bin import invoice
    from bin import clear
    from bin import usr_signup
    from bin import get_dirs

except ModuleNotFoundError:
    import mailer
    import invoice
    import voice_io
    import wolfy
    import clear
    import usr_signup
    import get_dirs
    
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
ct=(g.city)

#weather
def weather_curr():      
    api_key = "cd140d1c1404cba5de2dabf6bcd00f52" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "&q=" + ct + "&appid=" + api_key
    response = requests.get(url)  
    x = response.json()  
    if x["cod"] == "404":  
        voice_io.show("Oops! it looks like i ran into a problem fetching your request, maybe try again later?")
    else:
        y = x["main"]  
        curr_temperature = y["temp"]  
        curr_pressure = y["pressure"]  
        curr_humidity = y["humidity"]  
        z = x["weather"]  
        weather_desc = z[0]["description"]  
        voice_io.show(f"The current temperatre in {ct} is {str(round(curr_temperature-273))}°C" + ". It's a " +str(weather_desc))  

#weather forecaster
def weather_forec():
    voice_io.show("Sorry i am currently restricted to show weather forecast for tomorrow only. \nLook out for future updates and see if my handcuffs are set free. Here's tomorrow's weather forecast anyway.")
    owm = OWM('cd140d1c1404cba5de2dabf6bcd00f52')
    mgr=owm.weather_manager()
    loc = mgr.weather_at_place(ct)
    weather = loc.weather
    temp = weather.temperature(unit='celsius')
    for key,val in temp.items():
        if key=="temp":
            voice_io.show(f'\nThe temperature tommorow will be around {val}°C.')
        else:
            continue
    loa = mgr.forecast_at_place(ct,'3h')
    tomorrow=timestamps.tomorrow()
    forecasttt=loa.get_weather_at(tomorrow)
    status=(forecasttt.status)
    voice_io.show(f'And the sky would remain {status}')
#weather_forec(ct)

def date_con():
    d=date=datetime.datetime.now().strftime("%d") 
    m=date=datetime.datetime.now().strftime("%m") 
    y=date=datetime.datetime.now().strftime("%Y") 
    dt=[y,m,d]
    date=""
    for i in dt:
        date+=i
    date=int(date)
    return date

#Notes and Reminders

def note_write():   
    voice_io.input("Enter your mysql password")
    pas = invoice.inpt(processed = False)
    usr = usr_signup.info_out("mysql_usr")
    pwd = usr_signup.info_out("mysql_pswd")
    if pas != pwd:
        voice_io.show("The password you entered is incorrect! You are not authorised to complete this operation.")
    con=sql.connect(host="localhost",user=usr,password=pwd)
    cur=con.cursor()
    cur.execute("create database if not exists pydeskassist;")
    cur.execute("use pydeskassist;")
    cur.execute("create table if not exists notes(date_added date, note longtext);")
    voice_io.show("Okay so you wanna enter a new note? Here ya go!")
    x1=input("Enter Note Here: ")
    cur.execute("insert into notes values(curdate(), '%s');"%x1)
    voice_io.show("Note Saved Successfully!")
    con.commit()
    con.close()

    #note_write()
def reminder_write():
    voice_io.input("Enter your mysql password")
    pas = invoice.inpt(processed = False)
    usr = usr_signup.info_out("mysql_usr")
    pwd = usr_signup.info_out("mysql_pswd")
    if pas != pwd:
        voice_io.show("The password you entered is incorrect! You are not authorised to complete this operation.")
    con=sql.connect(host="localhost",user=usr,password=pwd)
    cur=con.cursor()
    cur.execute("create database if not exists pydeskassist;")
    cur.execute("use pydeskassist;")
    cur.execute("create table if not exists reminders(date_added date, reminder longtext, date_tbn date, time_tbn time);") #TBN- To Be Notified (OPTIONAL, well yes but actually no)
    x1=input("Enter Reminder: ")
    x2=input("Enter Date to be Notified (YYYYMMDD): ")
    x3=input("Enter Time to be Notified (HHMMSS): ")
    if x2=='' or x3=='':
        voice_io.show("Hey you left out a field empty that's not how reminders work mate, if this is how you wanna do it try the notes feature instead.")
    else:
        cur.execute("insert into reminders values(curdate(), '%s', '%s', '%s');"%(x1,x2,x3))
        voice_io.show("Reminder Saved Successfully!")
        con.commit()
    con.close()

def note_read():
    voice_io.input("Enter your mysql password")
    pas = invoice.inpt(processed = False)
    usr = usr_signup.info_out("mysql_usr")
    pwd = usr_signup.info_out("mysql_pswd")
    if pas != pwd:
        voice_io.show("The password you entered is incorrect! You are not authorised to complete this operation.")
    con=sql.connect(host="localhost",user=usr,password=pwd)
    cur=con.cursor()
    cur.execute("use pydeskassist;")
    cur.execute("select * from notes;")
    c=cur.fetchall()
    voice_io.show("Here are all your notes: ")
    voice_io.show(c)
    con.close()

    #note_read()

def reminder_read():
    voice_io.input("Enter your mysql password")
    pas = invoice.inpt(processed = False)
    usr = usr_signup.info_out("mysql_usr")
    pwd = usr_signup.info_out("mysql_pswd")
    if pas != pwd:
        voice_io.show("The password you entered is incorrect! You are not authorised to complete this operation.")
    con=sql.connect(host="localhost",user=usr,password=pwd)
    cur=con.cursor()
    cur.execute("use pydeskassist;")  
    voice_io.show("Hey there! Here's where all your reminders are stored! Yes I Know, I Know that i am not notifying you of your set reminders when the date and time comes but that's not a bug you see, my developers are still working on that feature which you might see in the near future ;) so for now you have to keep checking in here to keep up to date with your saved reminders. Sorry again for the inconvienience caused but anyway,")
    voice_io.show("\nWhat saved reminders do you want to read?")
    voice_io.show("1. Past Reminders")
    voice_io.show("2. Future/Upcoming Reminders")
    cho=input("Enter Choice: ")
    date=datetime.datetime.now().strftime("%x") 
    if cho=="1":
        cur.execute("select * from reminders where date_tbn < curdate();")
        c=cur.fetchall()
        voice_io.show("Here are all your past reminders: ")
        voice_io.show(c)
        if c=="[]":
            voice_io.show("Well it looks like you don't have any past reminders. Is that a good thing or a bad thing? Hmmm")

        else:
            z=input("Do you want to delete your past reminders? (Y/N) ")
            z=z.lower()
            if z=="y":
                cur.execute("delete from reminders where date_tbn < curdate();")
                con.commit()
                voice_io.show("Records Deleted Successfully!")
            elif z=="n":
                voice_io.show("Okay!")
            else:
                voice_io.show("Invalid Input!")

    elif cho=="2":
        cur.execute("select * from reminders where date_tbn >= curdate();")
        c=cur.fetchall()
        voice_io.show("Here are all your past reminders: ")
        voice_io.show(c)   
    else:
        voice_io.show('Invalid Input!')

    con.close()

#Time & Date
def date():
    x = datetime.datetime.now().strftime("%x")  
    voice_io.show(f"Today's date is {x}(MM/DD/YY)")
def time():
    x=datetime.datetime.now().strftime("%H:%M:%S")     
    voice_io.show(f"The current time is, {x}") 

def year():
    x=datetime.datetime.now()
    year = x.strftime("%Y")
    voice_io.show(f"The current year is {year}")

def month():
    x=datetime.datetime.now()
    month = x.strftime("%B")
    voice_io.show(f"The current month is {month}")

def day():
    x=datetime.datetime.now()
    day = x.strftime("%A")
    voice_io.show(f"Today it's {day}")

    #month()
    #day()
    #year()
    #time()
    #date()

#Send Emails

def sendEmail(): 
    mailer.mail_sender()
    
#sendEmail()

#Play Offline/Online Songs
def song_offline():
    voice_io.show("Alright, fetching your offline music playlist right away!")
    music_dir = get_dirs.MUSIC
    songs = os.listdir(music_dir)
    voice_io.show(songs)
    random = os.startfile(os.path.join(music_dir, songs[1]))
        
def song_online(query):    
    reg_ex = re.search('play (.+)', query)
    if reg_ex:
        song = reg_ex.group(1)
        url="https://www.youtube.com/results?search_query="
        url1=song.split()
        for i in range(len(url1)):
            url+=url1[i]
            if i!=-1:
                url+="+"
        #voice_io.show(url)
        voice_io.show("Your requested song will now be searched on youtube in your default browser! Make sure to click the first video link to play it. SORRY FOR THE INCONVINIENCE, We're Working on it.")
        webbrowser.open(url)
    else:
        voice_io.show("Uh-oh looks like i can't perform this operation right now, maybe try again later!")


#Web Search
def web(query):
    query=query.lower()
    if 'what is' in query:
        try:
            voice_io.show('Searching Wikipedia...\n')
            query1 = query.replace("what is ","")
            results = wikipedia.summary(query1)
            voice_io.show("According to Wikipedia,")
            voice_io.show(results)
        except:
            try:
                #clear.clear()
                voice_io.show(wolfy.wolfram_try(query))
            except:
                voice_io.show("Could not find any results relating to {query1}, \nplease make sure you're entering a valid input!")

    elif 'meaning of' in query:
        try:
            voice_io.show('Searching Wikipedia...')
            query1 = query.replace("meaning of ","")
            results = wikipedia.summary(query1,sentences=1)
            voice_io.show("According to Wikipedia")
            voice_io.show(results)
        except:
            try:
                #clear.clear()
                voice_io.show(wolfy.wolfram_try(query))
            except:
                voice_io.show("Could not find any results relating to {query1}, \nplease make sure you're entering a valid input!")
    
    elif 'define' in query:
        try:
            voice_io.show('Searching Wikipedia...')
            query1 = query.replace("define ","")
            results = wikipedia.summary(query1,sentences=1)
            voice_io.show("According to Wikipedia")
            voice_io.show(results)
        except:
            try:
                #clear.clear()
                voice_io.show(wolfy.wolfram_try(query))
            except:
                voice_io.show("Could not find any results relating to {query1}, \nplease make sure you're entering a valid input!")

    elif 'search' in query:
        query = query.replace("search ", "")
        voice_io.show(f"Searching google for '{query}'")
        query = query.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "where is" in query:
        query = query.replace("where is ", "")
        voice_io.show(f"Searching google maps for '{query}'")
        location = query
        voice_io.show("You asked to locate",location,"and here you go!")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "")

    elif "open" in query:
        reg_ex = re.search('open (.+)', query)
        if reg_ex:
            domain = reg_ex.group(1)
            #voice_io.show(domain)
            url='https://www.'+domain+".com"
            webbrowser.open(url)
            voice_io.show('The website you have requested will now be opened for you.')
        else:
            pass

    elif 'youtube' in query:
        voice_io.show("Alright, opening Youtube right away!\n")
        webbrowser.open("https://www.youtube.com")

    elif 'google' in query:
        voice_io.show("Alright, opening Google right away!\n")
        webbrowser.open("https://www.google.com")

    elif 'instagram' in query:
        voice_io.show("Alright, opening Instagram right away!")
        webbrowser.open("https://www.instagram.com")
    
    elif 'twitter' in query:
        voice_io.show("Alright, opening Twitter right away!")
        webbrowser.open("https://www.twitter.com")
    
    elif 'reddit' in query:
        voice_io.show("Alright, opening Reddit right away!")
        webbrowser.open("https://www.reddit.com")
    
    elif 'facebook' in query:
        voice_io.show("Alright, opening Facebook right away!")
        webbrowser.open("https://www.facebook.com")

    else:
        try:
            voice_io.show(wolfy.wolfram_try(query))
        except:
            voice_io.show("Uh-oh! It looks like i ran into some problems, why don't you try again later?")

#web()

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
            voice_io.show(x.decode())
    except Exception as e:
            voice_io.show(e)
            voice_io.show("Sorry couldn't fetch any record, maybe try again later.")
        
#news()