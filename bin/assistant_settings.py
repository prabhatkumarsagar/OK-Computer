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
assistant voice noise cancellation - none
assistant ui theme - light
assistant ui font - predefined 100%
"""
"""
import pickle
usr_ass_settings={}
as_vc_gnd=input("Enter the assistant voice gender: ") #DEF=MALE
as_vc_vol=int(input("Enter the assistant voice volume: ")) #DEF=1.0
as_vc_rate=int(input("Enter the assistant voice rate: ")) #DEF=200 wpm
as_vc_amb=input()
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