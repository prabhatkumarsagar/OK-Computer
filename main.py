from bin import file_operations
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
        input("\nAll packages have been successfully installed! Press Enter/Return to continue.")
        clear.clear()
    else:
        print("\nInstalling packages failed! Please try running this program again after resolving all the issues, and if the problem still persists, contact the developer.")
        exit()

    from bin import usr_signup
    from bin import voice_io
    from bin import invoice


file_user_data = get_dirs.FILE_USR_DATA
home = get_dirs.HOME
desktop = get_dirs.DESKTOP
downloads = get_dirs.DOWNLOADS
documents = get_dirs.DOCUMENTS
music = get_dirs.MUSIC
videos = get_dirs.VIDEOS
pictures = get_dirs.PICTURES


#clear_commands = ["clear", "clr", "clear screen", "clear terminal", "clearv current chats", "clear the terminal", "clear the session chat", "clear my screen", "clear "]
#print(path_user_data)
delete_file_unspecified = ["delete a file", "file delete", "remove a file",]
delete_folder_unspecified = ["delete a folder", "folder delete", "remove a folder", "remove directory", "rmdir"]
delete_general = ["delete", "del", "remove", "erase", "rm"]
rename_unspecified = ["rename a folder", "rename a file", "rename folder", "rename file", "folder rename", "file rename", "rename directory", "directory rename", "rname"]
copy = ["copy", "cp", "clone", "replicate"]

locate_desktop = ["1"]
locate_downloads = ["2"]
locate_documents = ["3"]
locate_music = ["4"]
locate_pictures = ["5"]
locate_videos = ["6"]
locate_home = ["7"]

sound = False

def main():
    global sound
    clear.clear()
    #this portion is dedicated to new-user sign-up
    if os.path.exists(file_user_data):
        #usr_data = open(path_user_data)
        pass

    else:
        sound = userSetup()

    usr_name = usr_signup.main(operation = "fetch", data_type = "name")

    clear.clear()
    voice_io.show(f"""Hey {usr_name}! 
        
What would you like me to do?""", sound = sound)

    while True:
        task = invoice.inpt()

        if task.lower() in delete_file_unspecified:
            deleteFileUnspecified()
        
        elif task.lower() in delete_folder_unspecified:
            deleteFolderUnspecified()

        elif task.lower() in delete_general:
            voice_io.show(f"What would you like to {task}, a file or a folder?")
            choice = invoice.inpt().lower()
            if choice == "file":
                deleteFileUnspecified()

            elif choice == "folder":
                deleteFolderUnspecified()

            else:
                voice_io.show("Unable to understand your command, please try again with the proper command.", sound = sound)
        
        elif task.lower in copy:
            search_dir = ""
            voice_io.show("Which file/folder would you like to delete?", sound = sound)
            folder_name = invoice.inpt()
            voice_io.show(f"Where would you like me to search for {folder_name}?\n1. Desktop\n2. Downloads\n3. Documents\n4. Music\n5. Pictures\n6. Videos\n7. Entire home directory", sound = sound)
            locate = invoice.inpt().lower()
            if locate in locate_desktop:
                search_dir = desktop

            elif locate in locate_documents:
                search_dir = documents

            elif locate in locate_downloads:
                search_dir = downloads

            elif locate in locate_home:
                search_dir = home
                        
            elif locate in locate_music:
                search_dir = music
            
            elif locate in locate_pictures:
                search_dir = pictures

            elif locate in locate_videos:
                search_dir = videos
                        
            else:
                voice_io.show("Selected directory does not exist, please try again!", sound = sound)
                            
            file_operations.deleteFolder(folder_name = folder_name,search_dir = search_dir)

        elif task.lower in rename:
    
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
Press Enter/Return to continue.
""", sound = True)
    command = invoice.inpt(iterate = False)


    if command == "disable sound":
        return_val =  False
    
    elif command == None:
        return_val =  True
    
    else:
        voice_io.show("Unable to understand your command, continuing with sound.")
    
    
    #if not os.path.exists(get_dirs.PATH_USR_DATA):
        #os.mkdir(get_dirs.PATH_USR_DATA)

    usr_signup.main(operation = "new", sound = return_val)
    return return_val

def deleteFileUnspecified():
    global sound
    search_dir = ""
    voice_io.show("Which file would you like to delete?", sound = sound)
    file_name = invoice.inpt()
    voice_io.show(f"Where would you like me to search for the file, {file_name}?\n1. Desktop\n2. Downloads\n3. Documents\n4. Music\n5. Pictures\n6. Videos\n7. Entire home directory", sound = sound)
    locate = invoice.inpt().lower()
    if locate in locate_desktop:
        search_dir = desktop

    elif locate in locate_documents:
        search_dir = documents

    elif locate in locate_downloads:
        search_dir = downloads

    elif locate in locate_home:
        search_dir = home
                
    elif locate in locate_music:
        search_dir = music
                
    elif locate in locate_pictures:
        search_dir = pictures

    elif locate in locate_videos:
        search_dir = videos
                
    else:
        voice_io.show("Selected directory does not exist, please try again!", sound = sound)
                    
    file_operations.deleteFile(file_name = file_name,search_dir = search_dir)

def deleteFolderUnspecified():
    global sound
    search_dir = ""
    voice_io.show("Which folder would you like to delete?", sound = sound)
    folder_name = invoice.inpt()
    voice_io.show(f"Where would you like me to search for the folder, {folder_name}?\n1. Desktop\n2. Downloads\n3. Documents\n4. Music\n5. Pictures\n6. Videos\n7. Entire home directory", sound = sound)
    locate = invoice.inpt().lower()
    if locate in locate_desktop:
        search_dir = desktop

    elif locate in locate_documents:
        search_dir = documents

    elif locate in locate_downloads:
        search_dir = downloads

    elif locate in locate_home:
        search_dir = home
                
    elif locate in locate_music:
        search_dir = music
    
    elif locate in locate_pictures:
        search_dir = pictures

    elif locate in locate_videos:
        search_dir = videos
                
    else:
        voice_io.show("Selected directory does not exist, please try again!", sound = sound)
                    
    file_operations.deleteFolder(folder_name = folder_name,search_dir = search_dir)


main()