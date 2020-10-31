import os
from os import system
import subprocess 
import datetime
import socket

from bin import get_dirs

try:
    import gtts
except:
    os.system("pip3 install gTTS")
    import gtts

try:
    from playsound import playsound
except:
    os.system("pip3 install playsound")
    from playsound import playsound
try:
    import pyttsx3
except:
    os.system("pip3 install pyttsx3")
    import pyttsx3

try:
    import speech_recognition as sr
except:
    os.system("pip3 install SpeechRecognition")
    import speech_recognition as sr


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)
engine.setProperty('rate',125) #Default Rate = 150

def voice_out(qry): 
    if is_connected():
        try:
            voice_ob = gtts.gTTS(qry)
            voice_ob.save(get_dirs.PATH_USR_DATA + "voice_output.mp3")
            playsound(get_dirs.PATH_USR_DATA + "voice_output.mp3")
            os.remove(get_dirs.PATH_USR_DATA + "voice_output.mp3")
        except:
            engine.say(qry) 
            engine.runAndWait()

    else:
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


def show(text = "", end = "\n", sep = " ", voice = True, show_output = True):
    if voice:
        if show_output:
            print(text, end = end, sep = sep)
        voice_out(text)
    else:
        if show_output:
            print(text, end = end, sep = sep)
    return text