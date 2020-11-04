import os

from bin import get_dirs
from bin import clear

try:
    #All the packages that require special dependencies, or depend on packages requiring them must be called from here.
    from bin import usr_signup
    from bin import voice_io
    from bin import invoice

except:
    from bin import install_packages as ip
    clear.clear()
    print("\nInstalling required packages.....\n")
    if ip.setup():
        input("\nAll packages have been successfully installed! Press Enter/Return to continue")
        clear.clear()
    else:
        print("\nInstalling packages failed! Please try running this program again after resolving all the issues, and if the problem still persists, contact the developer.")
        exit()

    from bin import usr_signup
    from bin import voice_io
    from bin import invoice


file_user_data = get_dirs.FILE_USR_DATA
#from bin import file_operations

#clear_commands = ["clear", "clr", "clear screen", "clear terminal", "clearv current chats", "clear the terminal", "clear the session chat", "clear my screen", "clear "]
#print(path_user_data)
voice_triggers = [""]
delete_unspecified = ["delete a file", "delete a folder", "file delete", "folder delete", "remove a file", "remove a folder", "remove directory"]
rename_unspecified = ["rename a folder", "rename a file", "rename folder", "rename file", "folder rename", "file rename", "rename directory", "directory rename"]

def main():
    sound = False
    clear.clear()
    #this portion is dedicated to new-user sign-up
    if os.path.exists(file_user_data):
        #usr_data = open(path_user_data)
        pass

    else:
        sound = userSetup()

    usr_name = usr_signup.main(operation = "fetch", data_type = "name")
    while True:
        clear.clear()
        voice_io.show(f"""Hey {usr_name}! 
        
What would you like me to do?
""", sound = sound)

        task = invoice.inpt()


        """if task.lower() in delete_unspecified:
            while True:
            voice_io.show("Which file/folder would you like to delete?", sound = sound)
            file_folder = input(">>>")
            voice_io.show("Where would you like me to search for the file?n1. \nDesktop\n2. Downloads\n3. Documents\n4. Music\n5. Pictures\n6. Videos\n7. Entire home directory")
            locate = input(">>>")
            locate = locate.lower()
            
            if locate in {""}"""

    #while True:
    


    
def userSetup():
    return_val = True
    voice_io.show("""Hii There!

I am Python, your personal desktop Assistant.
I will be present at all times, waiting for your command.
You can ask me to do what ever you want; getting some work done,
or lightening the mood with a few jokes or a friendly talk!

But first, please do let me know you better.
    
If you would like to disable sound, please type 'disable sound' and continue.
else you can simply continue by pressing Enter/Return and disable sound 
later on using the command 'disable sound'. You can also use the command 
'enable sound' if you feel generous enough to give me my voice(s) back!

You can always use the command 'voice' if you would prefer to speak your commands 
instead.
Press Ener/Return to continue.
""", sound = False)
    command = invoice.inpt()

    if command == "disable sound":
        return_val =  False
    
    elif command == "":
        return_val =  True
    
    else:
        voice_io.show("Unable to understand your command, continuing with sound.")
    
    
    if not os.path.exists(get_dirs.PATH_USR_DATA):
        os.mkdir(get_dirs.PATH_USR_DATA)

    usr_signup.main(operation = "new", sound = return_val)
    return return_val

main()
