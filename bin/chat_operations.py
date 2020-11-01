#chat operations go here!
import requests 
from bin import voice_io

#jokes
def joke():  
    res_j = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
    )
    if res_j.status_code == requests.codes.ok:
        voice_io.show('Here is an awesome one for you! ') #to be replaced with - aadeshSpeak("Here is an awesome one for you! ")
        voice_io.show(str(res_j.json()['joke'])) #to be replaced with - aadeshSpeak(str(res_j.json()['joke']))
    else:
        voice_io.show("Oops! it looks like i ran out of my jokes, why don't you try again later.") #to be replaced with - print("Oops! looks like i ran out of jokes, why don't you try again later.)

joke()

#help
#def help():
#    pass

#greet
def greet():
    pass