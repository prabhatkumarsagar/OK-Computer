#chat operations go here!

"""please note that all of the operations here has been migrated to the main.py file.
Thus any further modifications must be done in that file for convenience sake!"""

import random
import datetime
import requests
import voice_io
import usr_signup
import assistant_settings
import mailer

#jokes
def joke():  
    res_j = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
    )
    if res_j.status_code == requests.codes.ok:
        voice_io.show('Here is an awesome one for you! ') 
        voice_io.show(str(res_j.json()['joke'])) 
    else:
        voice_io.show("Oops! it looks like i ran out of my jokes, why don't you try again later.")

#joke()

#help
#1. Services Help
def srvc_help():
    voice_io.show("Alright, here goes my domain of expertise. \")")
    voice_io.show("1. I can open all sorts of websites and fetch web queries for you.")
    voice_io.show("2. I can open and close apps for you.")
    voice_io.show("3. I can open, rename, move and delete files and folders for you.")
    voice_io.show("4. I can read out today's news for you.")
    voice_io.show("5. I can tell you the current weather and the weather forecast for the next 7 days.")
    voice_io.show("6. I can manage your Notes and Reminders for you.")
    voice_io.show("7. I can send emails to your mail contacts for you.")
    voice_io.show("8. I can perform some calculations for you.")
    voice_io.show("9. I can play songs and even read out the date and time for you.")
    voice_io.show("10. Alas, I can even chit-chat with you :)")
    return

#2. Operations Help
def op_help():
    voice_io.show("Alright, So What operations do you need help with? (just enter the operation, for example 'news', and i'll tell you its general syntax and what it does too.)")
    x=input()
    x=x.lower()
    if "news" in x:
        voice_io.show("With the News operation you can ask me to read out the top 15 news headlines of the moment.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"Python tell me today's news\" OR \"Hey read out today's top headlines\" OR \"PDA NEWS!\" (YOU GET THE IDEA)")
        return
    elif "website" in x:
        voice_io.show("With the website operation you can ask me to open certain websites in your default browser.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"Python Open Youtube\" (BASIC WEBSITE OPENING) OR \"Open Instagram PDA\" (BASIC WEBSITE OPENING) OR \"Hey What is slavery?\" (WIKIPEDIA) OR  \"Define 'nuance'\" (GOOGLE SEARCH)")
        return
    elif "email" in x:
        voice_io.show("With this operation you can ask me to send an email to a contact of yours. Note: for this to function properly you must enter your email and password at the time of Sign Up. If you haven't correctly or want to change the same, use help.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"Python help me send an email\" OR \"Hey i need you to send an email\" (OR ANY OTHER SORT OF EMAIL QUERY)")
        return
    elif "song" in x:
        voice_io.show("With the website operation you can ask me to play both online and offline songs. Note: for offline songs, make sure that there are songs in the root Music Directory of your PC and in case of online songs, the song won't play automatically but instead you'll see a youtube page opened up with your song searched and you'll have to click on the first result yourself. SORRY FOR THE INCONVINIENCE, THIS WILL MOST LIKELY BE RECTIFIED IN THE COMING UPDATES. :D")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"Python Play Offline Songs\" OR \"PDA Play Genda Phool by Badshah\" OR \"Hey Play Arijit Singh's Songs\" (YOU GET THE IDEA)")
        return
    elif "weather" in x:
        voice_io.show("With this operation you can ask me about the current weather or the weather forecast for the next 7 days.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"Hey tell me the weather?\" OR \"What's the weather forecast for tomorrow?\" OR \"Python what's the temperature outside?\" OR \"PDA how's the josh?\" OR \"Tell me the weather forecast for the next 7 days\" (OR LITERALLY ANY OTHER WEATHER/WEATHER FORECAST/TEMPERATURE... QUERY)")
        return
    elif "time" in x or "date" in x:
        voice_io.show("With this operation you can ask me the current time and date.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"Hey tell me the time?\" OR \"What's the time?\" OR \"Python what's the time?\" OR \"PDA what's the time?\" OR \"Tell me the current time!\" (OR LITERALLY ANYTHING ELSE BUT JUST MAKE SURE \"TIME\" IS A PART OF THE QUERY)")
        voice_io.show("\"Hey tell me the date?\" OR \"What's today's date?\" OR \"Python what's the date?\" OR \"PDA what day is it?\" OR \"Tell me what month it is!\" (OR LITERALLY ANYTHING ELSE BUT JUST MAKE SURE \"DATE\"/\"DAY\"/\"MONTH\"/\"YEAR\" IS A PART OF THE QUERY)")
        return
    elif "calculation" in x:
        voice_io.show("With this you can ask me to perform mathematical operations like addition, subtraction and the likes.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"Hey what is 5 times 2?\" OR \"What is the square root of 25\" OR \"Python what's the cube of 69\" OR \"PDA what is 5 time 27 divided by 3\" (OR LITERALLY ANYTHING ELSE BUT JUST MAKE SURE THAT IT IS A MATHEMATICAL QUERY)")
        return
    elif "notes" in x or "reminders" in x:
        voice_io.show("With this operation you can ask me to save your notes and remind you of your reminders? haha.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"Python save a Note\" OR \"Save a Reminder PDA\" OR \"Python Add a Note\" (YOU GET THE IDEA)")
        return
    elif "joke" in x:
        voice_io.show("With the joke operation you can ask me to joke?")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"PDA tell me a joke\" OR \"Hey joke!!!\" OR \"Python i tell me something funny!\" OR ...")
        return
    elif "help" in x:
        voice_io.show("With the help operation you can ask me to help you around.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("\"PDA help\" OR \"Python help me\" OR \"Hey help me out\" OR ...")
        return
    elif "open file" in x:
        voice_io.show("With this operation you can ask me to open a file from a certain location for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Open filename from foldername/location")
        return
    elif "open folder" in x:
        voice_io.show("With this operation you can ask me to open a folder from a certain location for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Open foldername from foldername/location")
        return
    elif "close file" in x:
        voice_io.show("With this operation you can ask me to close an already opened file for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Close filename")
        return
    elif "close folder" in x:
        voice_io.show("With this operation you can ask me to close an already opened folder for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Close foldername")
        return
    elif "rename file" in x:
        voice_io.show("With this operation you can ask me to rename a file from a certain location for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Rename filename from foldername/location to newfilename")
        return
    elif "rename folder" in x:
        voice_io.show("With this operation you can ask me to rename a folder from a certain location for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Rename foldername from foldername/location to newfoldername")
        return
    elif "delete file" in x:
        voice_io.show("With this operation you can ask me to delete a file from a certain location for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Delete filename from foldername/location")
        return
    elif "delete folder" in x:
        voice_io.show("With this operation you can ask me to delete a folder from a certain location for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Delete foldername from foldername/location")
        return
    elif "move file" in x:
        voice_io.show("With this operation you can ask me to move a file from a certain location to another for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Move filename from foldername/location to newfoldername/newlocation")
        return
    elif "move folder" in x:
        voice_io.show("With this operation you can ask me to move a folder from a certain location to another for you.")
        voice_io.show("The General Syntax of this operation is: \n")
        voice_io.show("Move foldername from foldername/location to newfoldername/newlocation")
        return
    else:
        voice_io.show("Sorry i don't think i can help you with that!\nmake sure you're entering a valid operation name as an input, which is supposed to be one of the following: \n")
        voice_io.show("1. News")
        voice_io.show("2. Website")
        voice_io.show("3. Email")
        voice_io.show("4. Song")
        voice_io.show("5. Weather")
        voice_io.show("6. Time/Date")
        voice_io.show("7. Calculation")
        voice_io.show("8. Notes/Reminders")
        voice_io.show("9. Joke")
        voice_io.show("10. Help")
        voice_io.show("11. Open file")
        voice_io.show("12. Open folder")
        voice_io.show("13. Close file")
        voice_io.show("14. Close folder")
        voice_io.show("15. Rename file")
        voice_io.show("16. Rename folder")
        voice_io.show("17. Delete file")
        voice_io.show("18. Delete folder")
        voice_io.show("19. Move file")
        voice_io.show("20. Move folder")
        return

#3. Python Desktop Assistant Help (pda_help)
def pda_help():
    voice_io.show("Select from the following Settings which can i help you with?")
    voice_io.show("1. Assistant Settings Update")
    voice_io.show("2. Assitant Settings Reset")
    voice_io.show("3. User Data Update")    
    x=input("Enter Choice: ")
    if x=="1":
        assistant_settings.ass_settings_update()
    elif x=="2":
        assistant_settings.ass_settings_reset()
    elif x=="3":
        usr_signup.info_update()
    else:
        voice_io.show("Invalid Input! Please make sure you're entering a valid input!")

#feedback()
def feedback():
    mailer.feedback_sender()


def help():
    while True:
        voice_io.show("Hello Hello! What is it that i can help you with, today?")
        voice_io.show("1. Assistant Settings")
        voice_io.show("2. Assistant Services")
        voice_io.show("3. Assistant Operations")
        voice_io.show("4. Feedback (Suggest Improvements/Report Bugs/...)")
        voice_io.show("5. Exit")
        x=input("Enter Choice: ")
        if x=="1":
            pda_help()
            continue
        elif x=="2":
            srvc_help()
            continue
        elif x=="3":
            op_help()
            continue
        elif x=="4":
            feedback()
            continue
        elif x=="5":
            exit()
        else:
            voice_io.show("Invalid Input! Please Try Again!")
            continue


#greet
def gnd():
    if usr_signup.info_out("gender")=="Female":
        gndff=["Ma'am","Madam","Miss","Master"]
        return gndff[random.randint(0,3)]
    else:
        gndmm=["Sir","Mister","Master"]
        return gndmm[random.randint(0,2)]
gnd=gnd()

def greet():
    global gnd
    def gnd_hello(): 
        voice_io.show("Hello "+gnd)
        return

    def tm_hello():
        time=datetime.datetime.now().strftime("%H")  
        time=int(time)
        if time < 12:
            tm="Morning"
        elif 12 <= time < 18:
            tm="Afternoon"
        else:
            tm="Evening"
        voice_io.show("Good",tm,gnd)

    def talk():
        pass
    #tbdl
        
    #tm_hello()
    
#greet()  

#chat
#query=input("What you say: ")
def chat(query):
    query=query.lower()
    if "hello" in query:
        greet.gnd_hello()
        return
    elif "good" in query:
        greet.tm_hello()
        return
    elif "who are you" in query or "tell me about yourself" in query:
        print("I am your Personal Desktop Assistant, here to help you with your day to day tasks and queries. Why don't you try asking me something and i'll show you by practically doing it or not, hehe. ")
        return
    elif "who made you" in query or "who is your developer" in query or "who's your creator" in query or "who's your maker" in query or "who created you" or "who's your daddy" in query:
        print("I was made by Anirban Dutta and Prabhat Kumar Sagar as a part of their Computer Science School Project. Would you like to know more about them?")
        x=input()
        x=x.lower()
        if "yes" in x or "ok" in x or "yeah" in x:
            print("Alright!")
            webbrowser.open("https://github.com/prabhatkumarsagar")
            webbrowser.open("https://github.com/DuttaAB-dev")
            return
        elif "no" in x or "nope" in x or "not" in x:
            print("Alright!")
            return
        else:
            return

    elif "how are you" in query or "how do you do" in query or "how you doing" in query:
        print("Oh I am Grand, How are you master?")
        x=input()
        x=x.lower()
        if "good" in x or "great" in x or "fine" in x or "well" in x or "grand" in x or "nice" in x or "ok" in x or "okay" in x:
            print("Good to hear! Keep having fun!")
            return
        else:
            print("Well everything will be good soon, just keep smiling, it suits you.")
            return
    else:
        print("Well well well, i don't think i can help you with that?")
        return

