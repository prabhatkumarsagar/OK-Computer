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
import getpass
import tabulate
import time as samay
import notify2

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
import sqlite3 as sql
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


def time_now():
    t = samay.localtime() 
    time_now = samay.strftime("%Y-%m-%d %H:%M:%S", t)
    return time_now

def note_rem_create():
    con = sql.connect(get_dirs.DB_NOTES_REMINDERS)
    cur = con.cursor()
    cur.execute("create table if not exists notes(date_added date, note longtext);")
    cur.execute("create table if not exists past_reminders(datetime_added date, reminder longtext, datetime_tbn date);")
    cur.execute("create table if not exists future_reminders(datetime_added date, reminder longtext, datetime_tbn date);")
    con.close()

def note_write():
    note_rem_create()
    con = sql.connect(get_dirs.DB_NOTES_REMINDERS)
    cur = con.cursor()
    voice_io.show("Okay so you wanna enter a new note? Here ya go!")
    x1=invoice.inpt("Enter Note Here: ", processed = False)
    cur.execute("insert into notes values(datetime('now', 'localtime'), '%s');"%x1)
    voice_io.show("Note Saved Successfully!")
    con.commit()
    con.close()


def reminder_write():
    note_rem_create()
    con = sql.connect(get_dirs.DB_NOTES_REMINDERS)
    cur = con.cursor()
    x1=invoice.inpt("Enter Reminder: ")
    x2=invoice.inpt("Enter Date to be Notified (YYYY-MM-DD): ")
    x3=input("Enter Time to be Notified (HH:MM:SS): ")
    x4=x2+' '+x3
    datetime_now=time_now()

    if x4<datetime_now:
        prmpt=input("Hey you are entering a reminder for a date and time that has already passed, are you sure you want to continue? ")
        prmpt=prmpt.lower()
        if prmpt in ['yeah','yep','yes', 'ok']:
            voice_io.show("Alright as you wish, master!")
            cur.execute("insert into past_reminders values(datetime('now', 'localtime'), '%s', '%s');"%(x1,x4))
            voice_io.show("Reminder Saved Successfully!")
            con.commit()
        elif prmpt in ['no','nah','nope','not really']:
            voice_io.show("Okay!")
        else:
            voice_io.show("Invalid Input!")
    
    elif x4>datetime_now:
        cur.execute("insert into future_reminders values(datetime('now', 'localtime'), '%s', '%s');"%(x1,x4))
        voice_io.show("Reminder Saved Successfully!")
        con.commit()
        #reminder_remind()
    
    else:
        voice_io.show("An internal error occurred while processing your request, please make sure you've entered the values correctly and try again!")
    
    con.close()


def note_read():
    note_rem_create()
    con = sql.connect(get_dirs.DB_NOTES_REMINDERS)
    cur = con.cursor()
    cur.execute("select rowid, date_added, note from notes;")
    c=cur.fetchall()
    if c==[]:
        voice_io.show("There are no notes to be shown, try making new notes! :)")
    else:
        voice_io.show("Here are all your notes: ")
        print()
        voice_io.show(tabulate.tabulate(c, headers = ["NoteID","Date and Time Added", "Note"]))
        print()
        prmpt=input("Would you like to delete or edit these notes? ")
        prmpt=prmpt.lower()
        if prmpt in ['yeah','yep','yes', 'ok']:
            ch=int(input("\nAnd what do you want to do really? \n1. Edit \n2. Delete \nEnter Choice: "))
            if ch==1:
                noteid=int(input("Please Enter the NoteID of the Note you wanna edit: "))
                newnote=input("Now enter the new updated note: ")
                try:
                    cur.execute("update notes set note='%s' where rowid=%i;"%(newnote,noteid))
                    con.commit()
                    voice_io.show("Note Updated Successfully!")
                except:
                    voice_io.show("Sorry i couldn't process your request at the moment, maybe because you're not entering a valid NoteID or something else, why don't you try again later!?")

            elif ch==2:
                noteid=int(input("Please Enter the NoteID of the Note you wanna delete: "))
                try:
                    cur.execute("delete from notes where rowid=%i;"%(noteid))
                    con.commit()
                    voice_io.show("Note Deleted Successfully!")
                except:
                    voice_io.show("Sorry i couldn't process your request at the moment, maybe because you're not entering a valid NoteID or something else, why don't you try again later!?")

            else:
                voice_io.show("Invalid Input!")

        elif prmpt in ['no','nah','nope','not really']:
            voice_io.show("Alright!")

        else:
            print("Okay!")

    con.close()


def reminder_read():
    note_rem_create()
    con = sql.connect(get_dirs.DB_NOTES_REMINDERS)
    cur = con.cursor()
    voice_io.show("Hey there! Here's where all your reminders are stored! Yes I Know, I Know that i am not notifying you of your set reminders when the date and time comes but that's not a bug you see, my developers are still working on that feature and you'll see it in the near future ;) so just for now you have to keep checking in here to keep up to date with your saved reminders. Sorry again for the inconvienience caused but anyway,")
    voice_io.show("\nWhat reminders do you want to read?")
    voice_io.show("1. Past Reminders")
    voice_io.show("2. Future/Upcoming Reminders")
    cho=input("Enter Choice: ")
    if cho=="1":
        cur.execute("select rowid, datetime_added, reminder, datetime_tbn from past_reminders;")
        c=cur.fetchall()
        if c==[]:
            voice_io.show("Well it looks like you don't have any past reminders. Is that a good thing or a bad thing? Hmmm")

        else:
            voice_io.show("Here are all your past reminders: ")
            print()
            voice_io.show(tabulate.tabulate(c, headers = ["ReminderID","Date and Time Added", "Reminder", "Date and Time to be Notified"]))
            print()

            prmpt=input("Would you like to delete past reminders? ")
            prmpt=prmpt.lower()
            if prmpt in ['yeah','yep','yes', 'ok']:
                remid=input("Please Enter the ReminderID of the Reminder you wanna delete or type 'all' if you want to delete all of them: ")
                if remid.isnumeric()!=True:
                    remid=remid.lower()
                    if remid=='all':
                        cur.execute("delete from past_reminders;")
                        con.commit()
                        voice_io.show("All past reminders deleted successfully!")
                    else:
                        voice_io.show("Invalid Input!")       

                else: 
                    remid=int(remid)
                    try:
                        cur.execute("delete from past_reminders where rowid=%i;"%(remid))
                        con.commit()
                        voice_io.show("Reminder Deleted Successfully!")
                    except:
                        voice_io.show("Sorry i couldn't process your request at the moment, maybe because you're not entering a valid ReminderID or something else, why don't you try again later!?")


            elif prmpt in ['no','nah','nope','not really']:
                voice_io.show("Alright!")

            else:
                print("Okay!")



    elif cho=="2":
        cur.execute("select rowid, datetime_added, reminder, datetime_tbn from future_reminders;")
        c=cur.fetchall()
        if c==[]:
            voice_io.show("Well it looks like you don't have any upcoming reminders. Is that a good thing or a bad thing? Hmmm")

        else:
            voice_io.show("Here are all your upcoming/future reminders: ")
            print()
            voice_io.show(tabulate.tabulate(c, headers = ["ReminderID","Date and Time Added", "Reminder", "Date and Time to be Notified"]))
            print()

            prmpt=input("Would you like to edit or delete these reminders? ")
            prmpt=prmpt.lower()
            if prmpt in ['yeah','yep','yes', 'ok']:
                ch=int(input("\nAnd what do you want to do really? \n1. Edit \n2. Delete \nEnter Choice: "))
                if ch==1:
                    remid=int(input("Please Enter the ReminderID of the Reminder you wanna edit: "))
                    ch2=int(input("And What exactly do you wanna edit? \n1. Reminder Content \n2. Reminder Date and Time \nEnter Choice: "))
                    if ch2==1:
                        newrem=input("Okay Enter the new updated Reminder: ")
                        try:
                            cur.execute("update future_reminders set reminder='%s' where rowid=%i;"%(newrem,remid))
                            con.commit()
                            voice_io.show("Reminder Updated Successfully!")
                        except:
                            voice_io.show("Sorry i couldn't process your request at the moment, maybe because you're not entering a valid NoteID or something else, why don't you try again later!?")

                    elif ch2==2:
                        newdatetime=input("Okay Enter the new Date and Time (YYYY-MM-DD HH:MM:SS): ")
                        try:
                            cur.execute("update future_reminders set datetime_tbn='%s' where rowid=%i;"%(newdatetime,remid))
                            con.commit()
                            voice_io.show("Reminder Updated Successfully!")
                        except:
                            voice_io.show("Sorry i couldn't process your request at the moment, maybe because you're not entering a valid NoteID or something else, why don't you try again later!?")

                    else:
                        voice_io.show("Invalid Input")
                    
                elif ch==2:
                    remid=input("Please Enter the ReminderID of the Reminder you wanna delete or type 'all' if you want to delete all of them: ")
                    if remid.isnumeric()!=True:
                        remid=remid.lower()
                        if remid=='all':
                            cur.execute("delete from future_reminders;")
                            con.commit()
                            voice_io.show("All future reminders deleted successfully!")
                        else:
                            voice_io.show("Invalid Input!")       

                    else: 
                        remid=int(remid)
                        try:
                            cur.execute("delete from future_reminders where rowid=%i;"%(remid))
                            con.commit()
                            voice_io.show("Reminder Deleted Successfully!")
                        except:
                            voice_io.show("Sorry i couldn't process your request at the moment, maybe because you're not entering a valid ReminderID or something else, why don't you try again later!?")


            elif prmpt in ['no','nah','nope','not really']:
                voice_io.show("Alright!")

            else:
                print("Okay!")



    else:
        voice_io.show('Invalid Input!')

    con.close()


#okay so reminder_remind() works completely fine when standalone, but the problem now is that when we run it here, the while loop takes away the terminal executing the commands every second and thus it's a lot fucked up then it should've been! so rather than continuing with this right now imma give this a pause for now and work on it later and develop a script thingy that when reminder_remind() is called it is done in the background and whatever whatever. MULTITHREADING is prolly where the key to this prob lies.
"""
def reminder_remind():
    def notify(reminder):
        notify2.init("OK-Computer")
        n=notify2.Notification("Reminder", message=reminder)
        n.set_urgency(notify2.URGENCY_NORMAL)
        n.set_timeout(10000)
        n.show()

    def time_now():
        t = samay.localtime() 
        time_now = samay.strftime("%Y-%m-%d %H:%M:%S", t)
        return time_now

    while True:
        con = sql.connect(get_dirs.DB_NOTES_REMINDERS)
        cur = con.cursor()
        cur.execute("select datetime_tbn, reminder from future_reminders;")
        c=cur.fetchall()
        d1={}
        for i in c:
            d1[i[0]]=i[1]

        d2={}
        for i in sorted(d1.keys()):
            d2[i]=d1[i]
        if d2=={}:
            #print("No Upcoming Reminders!")
            break
        else:
            print(d2)
            for i in d2.keys():
                if i==time_now():
                    notify(d2[i])
                    cur.execute("delete from future_reminders where datetime_tbn='%s';"%i)
                    cur.execute("insert into past_reminders values(datetime('now','localtime'),'%s','%s');"%(d2[i],i))
                    con.commit()
                elif i<time_now():
                    notify(d2[i])
                    cur.execute("delete from future_reminders where datetime_tbn='%s';"%i)
                    cur.execute("insert into past_reminders values(datetime('now','localtime'),'%s','%s');"%(d2[i],i))
                    con.commit()
                else:
                    samay.sleep(1)
                    continue
        con.close()
"""


#Time & Date
def date():
    x = datetime.datetime.now().strftime("%d/%m/%Y")  
    voice_io.show(f"Today's date is {x} (DD/MM/YYYY)")

def time():
    #x=datetime.datetime.now().strftime("%H:%M:%S")    
    localtime = samay.localtime()
    x = samay.strftime("%I:%M:%S %p", localtime)
    voice_io.show(f"The current time is {x}") 

def year():
    x=datetime.datetime.now().strftime("%Y")
    voice_io.show(f"The current year is {x}")

def month():
    x=datetime.datetime.now().strftime("%B")
    voice_io.show(f"The current month is {x}") 

def day():
    x=datetime.datetime.now().strftime("%A")
    voice_io.show(f"Today it is a {x}")

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
            #clear.clear()
            voice_io.show(wolfy.wolfram_try(query))

        except:
            try:
                voice_io.show('Searching Wikipedia...\n')
                query1 = query.replace("what is ","")
                results = wikipedia.summary(query1)
                voice_io.show("According to Wikipedia,")
                voice_io.show(results)
            except:
                voice_io.show(f"Could not find any results relating to {query1}, \nplease make sure you're entering a valid input!")


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
                voice_io.show(f"Could not find any results relating to {query1}, \nplease make sure you're entering a valid input!")
    
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
                voice_io.show(f"Could not find any results relating to {query1}, \nplease make sure you're entering a valid input!")

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

    elif "open website" in query:
        reg_ex = re.search('open website (.+)', query)
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
            voice_io.show(x.decode(), end = "\n\n")
    except Exception as e:
            voice_io.show(e)
            voice_io.show("Sorry couldn't fetch any record, maybe try again later.")
        
#news()