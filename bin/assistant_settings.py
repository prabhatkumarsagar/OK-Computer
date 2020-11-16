import pickle as pk
from bin import voice_io
"""
Assistant Voice Settings:
- assistant voice gender (male/female) **WINDOWS ONLY
- assistant voice volume
- assistant voice rate
- assistant voice noise cancellation (ambient sounds)
- assistant voice language  **LINUX ONLY

Assistant UI Settings:
- assistant ui font **optional/if time allows/on later updates
- assistant ui theme **optional/if time allows/on later updates

DEFAULT VALUES:
assistant voice gender - Male
assistant voice language - English-India (en-in)
assistant voice volume - 100 (or System Default)
assistant voice rate - 120 
assistant ui theme - light
assistant ui font - predefined 100%
"""

"""
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices') 
for i in range(len(voices)):
    voice_io.show(voices[i])
engine.setProperty('voice',voices=="english")
engine.say("the quick brown fox jumped over the lazy dog")
engine.runAndWait()
"""
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
from bin.get_dirs import FILE_ASSISTANT_SETTINGS

usr_ass_settings={'vc_gnd':'male','vc_vol':1.0,'vc_rate':'100','vc_lng':'english-us'}

def write():
    f1=open(FILE_ASSISTANT_SETTINGS,"wb+")
    pk.dump(usr_ass_settings,f1)
    f1.close()
#write()

def read():
    f2=open(FILE_ASSISTANT_SETTINGS,"rb+")
    r=pk.load(f2)
    #voice_io.show(r)
    f2.close()
#read()

def update(x,y):
    f2=open(FILE_ASSISTANT_SETTINGS,"rb+")
    newc=pk.load(f2)
    f2.close()
    f3=open(FILE_ASSISTANT_SETTINGS,"wb+")
    newc[x]=y
    pk.dump(newc,f3)
    f3.close()
#update('vc_gnd','female')

def ass_settings_input():
    def vc_gnd_inp():
        as_vc_gnd=input("Enter the assistant voice gender (Male/Female): ") #DEF=MALE
        vc_gnd1=["male","man","boy","mister"]
        vc_gnd2=["female","girl","miss","missus","mrs","woman"]
        if as_vc_gnd.lower() in vc_gnd1:
            return "Male"
        elif as_vc_gnd in vc_gnd2:
            return "Female"
        else:
            voice_io.show("Invalid Input! Please Try Again!")
            vc_gnd_inp()
    #vc_gnd_inp()

    def vc_vol_inp():
        try:
            as_vc_vol=float(input("Enter the assistant voice volume (0-1): ")) #DEF=1.0
            if as_vc_vol >= 0 and as_vc_vol <= 1:
                return as_vc_vol
            else:
                voice_io.show("Invalid Input! Please Try Again!")
                return vc_vol_inp()
        except:
            voice_io.show("Invalid Input! Please Try Again!")
    #vc_vol_inp()

    def vc_rate_inp():
        try:
            as_vc_rate=int(input("Enter the assistant voice rate (Words per minute): ")) #DEF=200 wpm
            return as_vc_rate
        except:
            voice_io.show("Invalid Input! Please Try Again!")
            return vc_rate_inp()
    #vc_rate_inp()

    def vc_lng_inp():
        try:
            as_vc_lng=input("Enter the assistant voice language: ") 
            vc_lng1=["en-in","english","english india","english united states","english us"]
            if as_vc_lng.lower() in vc_lng1:
                as_vc_lng="english"
                #as_vc_lng_id=11
                return as_vc_lng
            else:
                as_vc_lng="Default"
                return as_vc_lng
        except:
            voice_io.show("Invalid Input! Please Try Again!")
            vc_lng_inp()
    #vc_lng_inp()
    usr_ass_settings['vc_gnd']=vc_gnd_inp()
    usr_ass_settings['vc_vol']=vc_vol_inp()
    usr_ass_settings['vc_rate']=vc_rate_inp()
    usr_ass_settings['vc_lng']=vc_lng_inp()
    write()
    read()
#ass_settings_input()


#UPDATE
def ass_settings_update():
    voice_io.show("What do you wanna update?")
    voice_io.show("1. Assistant Voice Gender")
    voice_io.show("2. Assistant Voice Volume")
    voice_io.show("3. Assistant Voice Rate")
    voice_io.show("4. Assistant Voice Language")
    voice_io.show("5. ")
    x=input("Enter Choice: ")
    if x=="1":
        u=input("Enter New Value(Male/Female): ")
        update('vc_gnd',u)
        read()
    elif x=="2":
        u=float(input("Enter New Value(0-1): "))
        update('vc_vol',u)
        read()
    elif x=="3":
        u=int(input("Enter New Value(Words Per Minute): "))
        update('vc_rate',u)
        read()
    elif x=="4":
        u=input("Enter New Value: ")
        update('vc_lng',u)
        read()
    else:
        voice_io.show("Invalid Input")
#ass_settings_update()

def ass_settings_reset():
    f4=open("assistant_settings.dat","wb+")
    pk.dump(usr_ass_settings,f4)
    f4.close()
    read()
#ass_settings_reset()

"""
while True:
     voice_io.show("What do you wanna do?")
     voice_io.show("1. New Assistant Settings")
     voice_io.show("2. Update Assistant Settings")
     voice_io.show("3. Reset Assistant Settings")
     voice_io.show("4. Exit")
    x=input("Enter CHOICE: ")
    if x=="1":
        ass_settings_input()
        break
    elif x=="2":
        ass_settings_update()
        break
    elif x=="3":
        ass_settings_reset()
        break
    elif x=="4":
        break
        exit()
    else:
         voice_io.show("Invalid Input! Please Try Again!")
        continue
"""

def first_run():
    ass_settings_input()