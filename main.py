import os

from bin import get_dirs
from bin import usr_signup
from bin import clear
from bin import voice_io

file_user_data = get_dirs.FILE_USR_DATA

#clear_commands = ["clear", "clr", "clear screen", "clear terminal", "clear current chats", "clear the terminal", "clear the session chat", "clear my screen", "clear "]
#print(path_user_data)
voice_triggers = [""]
delete_unspecified = ["delete a file", "delete a folder", "file delete", "folder delete", "remove a file", "remove a folder", "remove directory"]

def main():
    voice = True
    clear.clear()
    #this portion is dedicated to new-user sign-up
    if os.path.exists(file_user_data):
        #usr_data = open(path_user_data)
        pass

    else:
        voice = userSetup()

    usr_name = usr_signup.main(operation = "fetch", data_type = "name")
    while True:
        clear.clear()
        voice_io.show(f"""Hey {usr_name}! 
        
What would you like me to do?
""", voice = voice)

        task = input(">>>")

        if task.lower() in delete_unspecified:

        if "clear" in task.lower() or task.lower() == "clrcls":
            continue

        if task.lower() in "exitquitend":
            voice_io.show("\n\nBye and have a nice day!", voice = voice)
            exit()

    #while True:

    
def userSetup():
    return_val = True
    voice_io.show("""Hii There!

I am Python, your personal desktop Assistant.
I will be present at all times, waiting for your command.
You can ask me to do what ever you want; getting some work done,
or lightening the mood with a few jokes or a friendly talk!

But first, please do let me know you better.
    
If you would like to disable voice, please type 'disable voice' and continue.
else you can simply continue by pressing Enter/Return and disable voice 
later on using the command 'disable voice'.""")
    command = input(">>>")

    if command == "disable voice":
        return_val =  False
    
    elif command == "":
        return_val =  True
    
    else:
        voice_io.show("Unable to understand your command, continuing with voice")
    
    
    if not os.path.exists(get_dirs.PATH_USR_DATA):
        os.mkdir(get_dirs.PATH_USR_DATA)

    usr_signup.main(operation = "new", voice = return_val)
    return return_val

main()