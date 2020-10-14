import pyttsx3
import subprocess 
import speech_recognition as sr
import datetime
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',125)
engine.say('Hello there sire Prabhat how may i be of any fucking use today?')
engine.runAndWait()

"""
def speak(audio): 
    engine.say(audio) 
    engine.runAndWait()

def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Saturday 1 point o") 
    speak("I am your Personal Desktop Assistant") 
    speak(assname)
    usrname()

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except: 
        print(e)     
        print("Unable to Recognizing your voice.")   
        return "None"
      
    return query

def usrname(): 
    speak("What should i call you sir") 
    uname = takeCommand() 
    speak("Welcome Mister") 
    speak(uname) 
    print("Welcome Mr f'{uname}")
    speak("How can i Help you, Sir") 

wishMe()
"""