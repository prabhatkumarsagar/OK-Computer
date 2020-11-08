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
    print(voices[i])
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

usr_ass_settings={'vc_gnd':'male','vc_vol':1.0,'vc_rate':'200','vc_lng':'english-us'}
def ass_settings_default():
    global usr_ass_settings
    def vc_gnd_inp():
        as_vc_gnd=input("Enter the assistant voice gender (Male/Female): ") #DEF=MALE
        vc_gnd1=["male","man","boy","mister"]
        vc_gnd2=["female","girl","miss","missus","mrs","woman"]
        if as_vc_gnd.lower() in vc_gnd1:
            return "Male"
        elif as_vc_gnd in vc_gnd2:
            return "Female"
        else:
            print("Invalid Input! Please Try Again!")
            vc_gnd_inp()
    #vc_gnd_inp()

    def vc_vol_inp():
        try:
            as_vc_vol=float(input("Enter the assistant voice volume (0-1): ")) #DEF=1.0
            if as_vc_vol >= 0 and as_vc_vol <= 1:
                return as_vc_vol
            else:
                print("Invalid Input! Please Try Again!")
                return vc_vol_inp()
        except:
            print("Invalid Input! Please Try Again!")
    #vc_vol_inp()

    def vc_rate_inp():
        try:
            as_vc_rate=int(input("Enter the assistant voice rate (Words per minute): ")) #DEF=200 wpm
            return as_vc_rate
        except:
            print("Invalid Input! Please Try Again!")
            return vc_rate_inp()
    #vc_rate_inp()

    def vc_lng_inp():
        try:
            as_vc_lng=input("Enter the assistant voice language: ") 
            vc_lng1=["en-in","english","english india","english united states","english us"]
            if as_vc_lng.lower() in vc_lng1:
                as_vc_lng="english"
                as_vc_lng_id=11
                return as_vc_lng
            else:
                as_vc_lng="Default"
                as_vc_lng_id=10
                return as_vc_lng
        except:
            print("Invalid Input! Please Try Again!")
            vc_lng_inp()
    #vc_lng_inp()
    usr_ass_settings['vc_gnd']=vc_gnd_inp()
    usr_ass_settings['vc_vol']=vc_vol_inp()
    usr_ass_settings['vc_rate']=vc_rate_inp()
    usr_ass_settings['vc_lng']=vc_lng_inp()
    print(usr_ass_settings)
ass_settings_default()

#DISPLAY
def display():
    global usr_ass_settings
    print(usr_ass_settings)


#UPDATE
def ass_settings_update():
    global usr_ass_settings
    print("What do you wanna update?")
    print("1. Assistant Voice Gender")
    print("2. Assistant Voice Volume")
    print("3. Assistant Voice Rate")
    print("4. Assistant Voice Language")
    x=input("Enter Choice: ")
    if x=="1":
        u=input("Enter New Value(Male/Female): ")
        usr_ass_settings['vc_gnd']=u
        display()
    elif x=="2":
        u=float(input("Enter New Value(0-1): "))
        usr_ass_settings['vc_vol']=u
        display()
    elif x=="3":
        u=int(input("Enter New Value(Words Per Minute): "))
        usr_ass_settings['vc_rate']=u
        display()
    elif x=="4":
        u=input("Enter New Value: ")
        usr_ass_settings['vc_lng']=u
        display()
    else:
        print("Invalid Input")
ass_settings_update()