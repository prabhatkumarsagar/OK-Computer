#chat operations go here!
import requests 
import voice_io
import usr_signup

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
def syn_help():
    print("Hello Hello! What operations do you need help with? (just enter the operation, for example 'news', and i'll tell you its general syntax and what it does too)")
    x=input()
    if "news" in x:
        print("With the News operation you can ask me to read out the top 15 news headlines of the moment.")
        print("The General Syntax of this operation is: \n")
        print("")
    elif "website" in x:
        print("With the website operation you can ask me to open certain websites in your default browser.")
        print("The General Syntax of this operation is: \n")
        print("")
    elif "email" in x:
        print("With this operation you can ask me to send an email to a contact of yours. Note: for this to function properly you must enter your email and password at the time of Sign Up. If you haven't correctly or want to change the same, use help.")
        print("The General Syntax of this operation is: \n")
    elif "song" in x:
        print("With the website operation you can ask me to play both online and offline songs. Note: for offline songs, make sure that there are songs in the root Music Directory of your PC and in case of online songs, the song won't play automatically but instead you'll see a youtube page opened up with your song searched and you'll have to click on the first result yourself. SORRY FOR THE INCONVINIENCE, THIS WILL MOST LIKELY BE RECTIFIED IN THE COMING UPDATES. :D")
        print("The General Syntax of this operation is: \n")
    elif "weather" in x:
        print("With this operation you can ask me about the current weather or the weather forecast for the next 7 days.")
        print("The General Syntax of this operation is: \n")
    elif "time" in x or "date" in x:
        print("With this operation you can ask me the current time and date.")
        print("The General Syntax of this operation is: \n")
    elif "calculation" in x:
        print("With this you can ask me to perform mathematical operations like addition, subtraction and the likes.")
        print("The General Syntax of this operation is: \n")
    elif "notes" in x or "reminders" in x:
        print("With this operation you can ask me to save your notes and remind you of your reminders? haha.")
        print("The General Syntax of this operation is: \n")
    elif "" in x:
        pass
    else:
        pass
    #TBC


#greet
def greet():
    def hello():
        #print("Hello"+gnd)
        pass

    def help():
        print("Alright, here goes my domain of expertise. \")")
        print("1. I can open all sorts of websites and fetch web queries for you.")
        print("2. I can open and close apps for you.")
        print("3. I can open, rename, move and delete files and folders for you.")
        print("4. I can read out today's news for you.")
        print("5. I can tell you the current weather and the weather forecast for the next 7 days.")
        print("6. I can manage your Notes and Reminders for you.")
        print("7. I can send emails to your mail contacts for you.")
        print("8. I can perform some calculations for you.")
        print("9. I can play songs and even read out the date and time for you.")
        print("10. Alas, I can chit-chat with you, what else do you need eh? :)")
    
    def deede():
        pass


"""
if usr_signup.info_out("gender")=="Female":
    print("Hello Mam")
else:
    print("Hello Sir")
"""