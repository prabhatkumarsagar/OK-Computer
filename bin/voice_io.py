import pyttsx3
import subprocess 
import speech_recognition as sr
import datetime
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)
engine.setProperty('rate',125) #Default Rate = 150

def voice_out(qry): 
    engine.say(qry) 
    engine.runAndWait()

def chng_voice_rate(newrate):
    engine.setProperty('rate',newrate)

def chng_voice_lang(x):
    engine.setProperty('voice',voices[x].id)

"""
VOICE IDS
german 8
default 10
english 11
english-us 16
spanish 19
french 26
hindi 29
malayalam 46
punjabi 51
russian 56
tamil 62
Mandarin 67
"""


def voice_in():
    r = sr.Recognizer() 
    with sr.Microphone() as source:  
        print("speak now")
        audio = r.listen(source) 
   
    try:    
        query = r.recognize_google(audio, language ='en-in') 
        print("you said: ",query)

    except:   
        print("Sorry i didn't get that! Please try again.")   


voice_in()