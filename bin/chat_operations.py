#chat operations go here!
import requests 

#jokes
def joke():  
    res_j = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
    )
    if res_j.status_code == requests.codes.ok:
        print('Here is an awesome one for you! ')
        print(str(res_j.json()['joke'])) 
    else:
        print("Oops! it looks like i ran out of my jokes, why don't you try again later.")

joke()

#help
#def help():
#    pass

#greet
def greet():
    pass