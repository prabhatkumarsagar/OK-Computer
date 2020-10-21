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

usr_ass_settings={'vc_gnd':'male','vc_vol':1.0,'vc_rate':'200','vc_lng':'english-us'}
as_vc_gnd=input("Enter the assistant voice gender: ") #DEF=MALE
as_vc_vol=float(input("Enter the assistant voice volume: ")) #DEF=1.0
as_vc_rate=int(input("Enter the assistant voice rate: ")) #DEF=200 wpm
as_vc_lng=input("Entet the assistant voice language: ") #DEF=en-in
usr_ass_settings['vc_gnd']=as_vc_gnd
usr_ass_settings['vc_vol']=as_vc_vol
usr_ass_settings['vc_rate']=as_vc_rate
usr_ass_settings['vc_lng']=as_vc_lng
#print(usr_ass_settings)

def ass_settings_update():
    print("What do you wanna update?")
    print("1. Assistant Voice Gender")
    print("2. Assistant Voice Volume")
    print("3. Assistant Voice Rate")
    print("4. Assistant Voice Language")
    ch=input("Enter Choice: ")
    if ch==1:
        u=input("Enter New Value(Male/Female): ")
        usr_ass_settings['vc_gnd']=u
    elif ch==2:
        u=float(input("Enter New Value(0-1): "))
        usr_ass_settings['vc_vol']=u
    elif ch==3:
        u=int(input("Enter New Value(No. of Words Per Minute): "))
        usr_ass_settings['vc_rate']=u
    elif ch==4:
        u=input("Enter New Value: ")
        usr_ass_settings['vc_lng']=u
    else:
        print("Invalid Input")

#NEEDS SOME BUG FIXING AND STRUCTURING HERE AND THERE