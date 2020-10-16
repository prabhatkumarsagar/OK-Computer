#chat operations goes here!
import requests 

#jokes
def joke():     #to be replaced with - elif 'joke' in query: / to be added later 
    res_j = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
    )
    if res_j.status_code == requests.codes.ok:
        print('Here is an awesome one for you! ') #to be replaced with - aadeshSpeak("Here is an awesome one for you! ")
        print(str(res_j.json()['joke'])) #to be replaced with - aadeshSpeak(str(res_j.json()['joke']))
    else:
        print("Oops! it looks like i ran out of my jokes, why don't you try again later.") #to be replaced with - print("Oops! looks like i ran out of jokes, why don't you try again later.)

#joke()