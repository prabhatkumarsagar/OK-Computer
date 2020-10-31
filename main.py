import os

from bin import get_dirs
from bin import usr_signup
from bin import clear
from bin import voice_io

voice_io.voice_out('hello there')

file_user_data = get_dirs.FILE_USR_DATA

#clear_commands = ["clear", "clr", "clear screen", "clear terminal", "clear current chats", "clear the terminal", "clear the session chat", "clear my screen", "clear "]
#print(path_user_data)
voice_triggers = [""]

def main():
    clear.clear()
    #this portion is dedicated to new-user sign-up
    if os.path.exists(file_user_data):
        #usr_data = open(path_user_data)
        pass

    else:
        userSetup()

    usr_name = usr_signup.main(operation = "fetch", data_type = "name")
    while True:
        clear.clear()
        print(f"""Hey {usr_name}! 
        
What would you like me to do?
""")

        task = input(">>>")

        if 

        if "clear" in task.lower() or task.lower() == "clrcls":
            continue

        if task.lower() in "exitquitend":
            print("\n\nBye and have a nice day!")
            exit()

    #while True:
        

    
def userSetup():
    input("""Hii There!

I am Python, your personal desktop Assistant.
I will be present at all times, waiting for your command.
You can ask me to do what ever you want; getting some work done.
or lightening the mood with a few jokes or a friendly talk!

But first, please do let me know you better.
    
Please press Enter/Return to Continue.""")
    if not os.path.exists(get_dirs.PATH_USR_DATA):
        os.mkdir(get_dirs.PATH_USR_DATA)
    usr_signup.main(operation = "new")

main()