#chat operations go here!
import requests 
import voice_io
import usr_signup

#jokes
def joke():  
    res_j = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
    )
    if res_j.status_code == requests.codes.ok:
        voice_io.show('Here is an awesome one for you! ') 
        voice_io.show(str(res_j.json()['joke'])) 
    else:
        voice_io.show("Oops! it looks like i ran out of my jokes, why don't you try again later.")

#joke()

#help
def help():
    """
    You can use these commands and I'll help you out:
    1. Open reddit subreddit : Opens the subreddit in default browser.
    2. Open xyz.com : replace xyz with any website name
    3. Send email/email : Follow up questions such as recipient name, content will be asked in order.
    4. Current weather in {cityname} : Tells you the current condition and temperture
    5. Hello
    6. play me a video : Plays song in your VLC media player
    7. change wallpaper : Change desktop wallpaper
    8. news for today : reads top news of today
    9. time : Current system time
    10. top stories from google news (RSS feeds)
    11. tell me about xyz : tells you about xyz
    """

#greet
def greet():
    def hello():
        print("Hello"+gnd)


"""
if usr_signup.info_out("gender")=="Female":
    print("Hello Mam")
else:
    print("Hello Sir")
"""