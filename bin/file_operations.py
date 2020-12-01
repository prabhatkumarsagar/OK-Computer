#file operations go here! 
#file handler
from importlib.abc import FileLoader
import os
import shutil
import multiprocessing
from playsound import playsound
from bin import get_dirs
from bin import voice_io
from bin import invoice

audio_file_ext = [".pcm", ".wav", ".aiff", ".mp3", ".aac", ".ogg", ".wma", ".flac", ".alac", ".wma"]

def fileSearch(file_name, search_dir):
#Searches for the given file name in the file tree(case sensitive)
    results = []
    for root, dirs, files in os.walk(search_dir): 
        for file in files:
            if file_name in file:  
                results.append({"root": root, "file": file})

    return  results
    
def folderSearch(folder_name, search_dir):
#Searches for the given folder name in the file tree(case sensitive)
    results = []
    for root, dirs, files in os.walk(search_dir): 
        for folder in dirs:
            if  folder_name in folder:  
                results.append({"root": root, "folder": folder})

    return  results
    
def deleteFile(file_name,search_dir):
    file_search_results = fileSearch(file_name, search_dir)
    if file_search_results != []:
        if len(file_search_results) == 1:
            invoice.inpt("%s from %s will be permanently lost, press Enter to continue."%(file_search_results[0]["file"], file_search_results[0]["root"]), iterate = False)
            os.remove(file_search_results[0]["root"] + "/" + file_search_results[0]["file"])
            voice_io.show(file_name," has been deleted successfully!")
            
        else:
            n_results = len(file_search_results)
            voice_io.show(f"Found {n_results} files matching the given file name! They are :-")
            sno = 1
            for i in file_search_results:
                voice_io.show(f"{sno}. file '{i['file']}', inside '{i['root']}'")
                sno += 1
            voice_io.show("Select the number of the file which you would like to delete")
            choice = int(invoice.inpt())
            choice -= 1
            try:
                f_name = file_search_results[choice]['file']
                parent_dir = file_search_results[choice]['root']
                invoice.inpt(f"'{f_name}' from '{parent_dir}' will be permanently lost, press Enter to continue.", iterate = False)
                os.remove(parent_dir + "/" + f_name)
                voice_io.show(f"'{f_name}' has been deleted successfully!")

            except IndexError:
                voice_io.show("Deletion failed : Sorry, but the entered number is not within the range of available options.")
            
            except SyntaxError or TypeError:
                voice_io.show("Deletion failed : Sorry, but your entered data is not a number.")

    else:
        voice_io.show(f"Sorry, could not find file '{file_name}', please check if the file you named exists or\nhas been spelled correctly.")

def deleteFolder(folder_name, search_dir):
    folder_search_results = folderSearch(folder_name, search_dir)
    if folder_search_results != []:
        if len(folder_search_results) == 1:
            invoice.inpt("%s from %s will be permanently lost, press Enter to continue."%(folder_search_results[0]["folder"], folder_search_results[0]["root"]), iterate = False)
            os.rmdir(folder_search_results[0]["root"] + "/" + folder_search_results[0]["folder"])
            voice_io.show(folder_name,"has been deleted successfully!")
            
        else:
            n_results = len(folder_search_results)
            voice_io.show(f"Found {n_results} folder matching the given folder name! They are :-")
            sno = 1
            for i in folder_search_results:
                voice_io.show(f"{sno}. folder '{i['folder']}', inside '{i['root']}'")
                sno += 1
            voice_io.show("Select the number of the folder which you would like to delete")
            choice = int(invoice.inpt())
            choice -= 1
            try:
                f_name = folder_search_results[choice]['folder']
                parent_dir = folder_search_results[choice]['root']
                invoice.inpt(f"'{f_name}' from '{parent_dir}' will be permanently lost, press Enter to continue.", iterate = False)
                os.remove(parent_dir + "/" + f_name)
                voice_io.show(f"'{f_name}' has been deleted successfully!")

            except IndexError:
                voice_io.show("Deletion failed : Sorry, but the entered number is not within the range of available options.")
            
            except SyntaxError or TypeError:
                voice_io.show("Deletion failed : Sorry, but your entered data is not a number.")

    else:
        voice_io.show(f"Sorry, could not find file '{folder_name}', please check if the file you named exists or\nhas been spelled correctly.")

def copy(obj_name, search_dir, dest_dir):
    dest_dir = get_dirs.HOME + "/" + dest_dir
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)

    folder_search_results = folderSearch(obj_name, search_dir)
    file_search_results = fileSearch(obj_name, search_dir)
    if folder_search_results != [] and file_search_results != 0:
        count_files = len(file_search_results)
        count_folders = len(folder_search_results)
        voice_io.show(f"Found {count_files} files and {count_folders} folders matching the given name! They are :-")
        sno = 1
        for i in file_search_results:
            voice_io.show(f"{sno}. file '{i['file']}', inside '{i['root']}'")
            sno += 1
        
        for i in folder_search_results:
            voice_io.show(f"{sno}. folder '{i['folder']}', inside '{i['root']}'")
            sno += 1
        voice_io.show("Select the number of the file/folder which you would like to copy.")
        choice = int(invoice.inpt())
        choice -= 1
        try:
            if choice in range(count_files):
                f_name = file_search_results[choice]['file']
                parent_dir = file_search_results[choice]['root']
                voice_io.show(f"Copying file '{f_name}' from '{parent_dir}' to '{dest_dir}'.....")
                shutil.copy2(parent_dir + "/" + f_name, dest_dir)
                voice_io.show(f"Successfully copied '{f_name}' to '{dest_dir}'!")
            
            elif choice - (count_files - 1) in range(count_folders):
                choice -= (count_files - 1)
                f_name = folder_search_results[choice]['folder']
                parent_dir = folder_search_results[choice]['root']
                voice_io.show(f"Copying folder '{f_name}' from '{parent_dir}' to '{dest_dir}'.....")
                shutil.copy2(parent_dir + "/" + f_name, dest_dir)
                voice_io.show(f"Successfully copied '{f_name}' to '{dest_dir}'!")

            else:
                voice_io.show("Copying failed : Sorry, but the entered number is not within the range of available options.")
            
        except SyntaxError or TypeError:
            voice_io.show("Copying failed : Sorry, but your entered data is not a number.")

    elif folder_search_results != []:
        if len(folder_search_results) == 1:
            voice_io.show(f"Copying folder '{folder_search_results[0]['folder']}' from '{folder_search_results[0]['root']}' to '{dest_dir}'.....")
            shutil.copy2(folder_search_results[0]["root"] + "/" + folder_search_results[0]["folder"], dest_dir)
            voice_io.show(f"Successfully copied '{folder_search_results[0]['file']}' to '{dest_dir}'!")
        
        else:
            sno = 1
            for i in folder_search_results:
                voice_io.show(f"{sno}. folder '{i['folder']}', inside '{i['root']}'")
                sno += 1
            voice_io.show("Select the number of the folder which you would like to copy.")
            choice = int(invoice.inpt())
            choice -= 1
            try:
                f_name = folder_search_results[choice]['folder']
                parent_dir = folder_search_results[choice]['root']
                voice_io.show(f"Copying folder '{f_name}' from '{parent_dir}' to '{dest_dir}'.....")
                shutil.copy2(parent_dir + "/" + f_name, dest_dir)
                voice_io.show(f"Successfully copied '{f_name}' to '{dest_dir}'!")

            except IndexError:
                voice_io.show("Copying failed : Sorry, but the entered number is not within the range of available options.")
                
            except SyntaxError or TypeError:
                voice_io.show("Copying failed : Sorry, but your entered data is not a number.")  
    
    elif file_search_results != []:
        if len(file_search_results) == 1:
            voice_io.show(f"Copying file '{file_search_results[0]['file']}' from '{file_search_results[0]['root']}' to '{dest_dir}''.....")
            shutil.copy2(file_search_results[0]["root"] + "/" + file_search_results[0]["file"], dest_dir)
            voice_io.show(f"Successfully copied '{file_search_results[0]['file']}' to '{dest_dir}'!")

        else:
            sno = 1
            for i in file_search_results:
                voice_io.show(f"{sno}. file '{i['file']}', inside '{i['root']}'")
                sno += 1
            voice_io.show("Select the number of the file which you would like to copy.")
            choice = int(invoice.inpt())
            choice -= 1
            try:
                f_name = file_search_results[choice]['file']
                parent_dir = file_search_results[choice]['root']
                voice_io.show(f"Copying file '{f_name}' from '{parent_dir}' to '{dest_dir}'.....")
                shutil.copy2(parent_dir + "/" + f_name, dest_dir)
                voice_io.show(f"Successfully copied '{f_name}' to '{dest_dir}'!")

            except IndexError:
                voice_io.show("Copying failed : Sorry, but the entered number is not within the range of available options.")
                
            except SyntaxError or TypeError:
                voice_io.show("Copying failed : Sorry, but your entered data is not a number.") 

    else:
        voice_io.show("Sorry, could not find file/folder '{obj_name}'!")

def rname(obj_name, new_name, search_dir):
    folder_search_results = folderSearch(obj_name, search_dir)
    file_search_results = fileSearch(obj_name, search_dir)
    new_file_name = ""
    new_ext = ""
    old_file_name = ""
    old_ext = ""
    
    if folder_search_results != [] and file_search_results != []:
        count_files = len(file_search_results)
        count_folders = len(folder_search_results)
        voice_io.show(f"Found {count_files} files and {count_folders} folders matching the given name! They are :-")
        sno = 1
        for i in file_search_results:
            voice_io.show(f"{sno}. file '{i['file']}', inside '{i['root']}'")
            sno += 1
        
        for i in folder_search_results:
            voice_io.show(f"{sno}. folder '{i['folder']}', inside '{i['root']}'")
            sno += 1
        voice_io.show("Select the number of the file/folder which you would like to rename.")
        choice = int(invoice.inpt())
        choice -= 1
        try:
            if choice in range(count_files):                
                f_name = file_search_results[choice]['file']
                new_name = new_name.split('.')
                new_file_name = new_name[0]
                if len(new_name) > 2:
                    for i in range(1, len(new_name) - 2):
                        new_file_name += "." + new_name[i]
                
                if len(new_name) > 1:
                    new_ext = new_name[len(new_name) - 1]
                    if new_ext == new_file_name:
                        new_ext = ""

                if len(f_name.split(".")) > 1:
                    old_ext = f_name.split(".")[len(f_name.split(".")) - 1]
                    if new_ext == "" and old_ext != f_name.split('.')[0]:
                        new_ext = old_ext

                new_full_name = new_file_name + "." + new_ext

                parent_dir = file_search_results[choice]['root']
                voice_io.show(f"Renaming file '{f_name}' from '{parent_dir}' to '{new_full_name}'.....")
                os.rename(parent_dir + "/" + f_name, parent_dir + "/" + new_full_name)
                voice_io.show(f"Successfully renamed '{f_name}' to '{new_full_name}'!")
            
            elif choice - (count_files - 1) in range(count_folders):
                choice -= (count_files - 1)
                f_name = folder_search_results[choice]['folder']
                parent_dir = folder_search_results[choice]['root']
                voice_io.show(f"Renaming folder '{f_name}' from '{parent_dir}' to '{new_name}''.....")
                os.rename(parent_dir + "/" + f_name, parent_dir + "/" + new_name)
                voice_io.show(f"Successfully renamed '{f_name}' to '{new_name}'!")

            else:
                voice_io.show("Renaming failed : Sorry, but the entered number is not within the range of available options.")
            
        except SyntaxError or TypeError:
            voice_io.show("Renaming failed : Sorry, but your entered data is not a number.")

    elif folder_search_results != []:
        if len(folder_search_results) == 1:
            parent_dir = folder_search_results[0]["root"]
            f_name = folder_search_results[0]["folder"]
            voice_io.show(f"Renaming folder '{folder_search_results[0]['folder']}' from '{folder_search_results[0]['root']}' to '{new_name}'.....")
            os.rename(parent_dir + "/" + f_name, parent_dir + "/" + new_name)
            voice_io.show(f"Successfully renamed '{folder_search_results[0]['folder']}' to '{new_name}'!")
        
        else:
            sno = 1
            for i in folder_search_results:
                voice_io.show(f"{sno}. folder '{i['folder']}', inside '{i['root']}'")
                sno += 1
            voice_io.show("Select the number of the folder which you would like to rename.")
            choice = int(invoice.inpt())
            choice -= 1
            try:
                f_name = folder_search_results[choice]['folder']
                parent_dir = folder_search_results[choice]['root']
                voice_io.show(f"Renaming folder '{f_name}' from '{parent_dir}' to '{new_name}'.....")
                os.rename(parent_dir + "/" + f_name, parent_dir + "/" + new_name)
                voice_io.show(f"Successfully renamed '{f_name}' to '{new_name}'!")

            except IndexError:
                voice_io.show("Renaming failed : Sorry, but the entered number is not within the range of available options.")
                
            except SyntaxError or TypeError:
                voice_io.show("Renaming failed : Sorry, but your entered data is not a number.")  
    
    elif file_search_results != []:
        if len(file_search_results) == 1:
            parent_dir = file_search_results[0]["root"]
            f_name = file_search_results[0]["file"]
            new_name = new_name.split('.')
            new_file_name = new_name[0]
            if len(new_name) > 2:
                for i in range(1, len(new_name) - 2):
                    new_file_name += "." + new_name[i]

            if len(new_name) > 1:
                new_ext = new_name[len(new_name) - 1]
                if new_ext == new_file_name:
                    new_ext = ""
            
            if len(f_name.split(".")) > 1:
                old_ext = f_name.split(".")[len(f_name.split(".")) - 1]
                if new_ext == "" and old_ext != f_name.split('.')[0]:
                    new_ext = old_ext
                
            new_full_name = new_file_name + "." + new_ext

            voice_io.show(f"Renaming file '{file_search_results[0]['file']}' from '{file_search_results[0]['root']}' to '{new_full_name}''.....")
            os.rename(parent_dir + "/" + f_name, parent_dir + "/" + new_full_name)
            voice_io.show(f"Successfully renamed '{file_search_results[0]['file']}' to '{new_full_name}'!")

        else:
            sno = 1
            for i in file_search_results:
                voice_io.show(f"{sno}. file '{i['file']}', inside '{i['root']}'")
                sno += 1
            voice_io.show("Select the number of the file which you would like to rename.")
            choice = int(invoice.inpt())
            choice -= 1
            try:
                f_name = file_search_results[choice]['file']
                new_name = new_name.split('.')
                new_file_name = new_name[0]
                if len(new_name) > 2:
                    for i in range(1, len(new_name) - 2):
                        new_file_name += "." + new_name[i]

                if len(new_name) > 1:
                    new_ext = new_name[len(new_name) - 1]
                    if new_ext == new_file_name:
                        new_ext = ""
                
                if len(f_name.split(".")) > 1:
                    old_ext = f_name.split(".")[len(f_name.split(".")) - 1]
                    if new_ext == "" and old_ext != f_name.split('.')[0]:
                        new_ext = old_ext
                    
                new_full_name = new_file_name + "." + new_ext

                parent_dir = file_search_results[choice]['root']
                voice_io.show(f"Renaming file '{f_name}' from '{parent_dir}' to '{new_full_name}'.....")
                os.rename(parent_dir + "/" + f_name, parent_dir + "/" + new_full_name)
                voice_io.show(f"Successfully renamed '{f_name}' to '{new_full_name}'!")

            except IndexError:
                voice_io.show("Renaming failed : Sorry, but the entered number is not within the range of available options.")
                
            except SyntaxError or TypeError:
                voice_io.show("Renaming failed : Sorry, but your entered data is not a number.") 

    else:
        voice_io.show("Sorry, could not find file/folder '{obj_name}'!")

def createFile(f_name, path, type):
    path = get_dirs.HOME + '/' + path
    os.mkdir(path)
    if type == "txt":
        f = open(f_name + ".txt", "w")
        f.close()
    
    if type == "doc":
        f = open(f_name + ".docx", "w")
        f.close()

    if type == "ppt":
        f = open(f_name + ".pptx", "w")
        f.close()
    
    if type == "sheet":
        f = open(f_name + ".xls", "w")
        f.close()

def playMusic(name, search_dir):
    file_search_results = fileSearch(file_name = name, search_dir = search_dir)
    music_files = []
    if len(file_search_results) > 0:
        for file_obj in file_search_results:
            f_name = file_obj['file']
            for ext in audio_file_ext:
                if ext in f_name:
                    music_files.append(file_obj)
                    break

        if len(music_files) == 1:
            f_name = music_files[0]['file']
            directory = music_files[0]['root']
            f_path = directory + '/' + f_name
            voice_io.show(f"Playing the audio file '{f_name}' from '{directory}'.")
            p = multiprocessing.Process(target=playsound, args=(f_path,))
            p.start()
            input("Press ENTER to stop playback")
            p.terminate()
            voice_io.show(f"Stopped playing '{f_name}'.")

        elif len(music_files) > 1:
            sno = 1
            voice_io.show(f"Found {len(music_files)} files matching the given file name :-")
            for i in music_files:
                voice_io.show(f"{sno}. file '{i['file']}', inside '{i['root']}'")
                sno += 1
            voice_io.show("Select the number of the audio file which you would like to play.")
            choice = int(invoice.inpt())
            choice -= 1
            try:
                f_name = music_files[choice]['file']
                directory = music_files[choice]['root']
                f_path = directory + "/" + f_name
                voice_io.show(f"Playing the audio file '{f_name}' from '{directory}'.")
                p = multiprocessing.Process(target=playsound, args=(f_path,))
                p.start()
                input("Press ENTER to stop playback")
                p.terminate()
                voice_io.show(f"Stopped playing '{f_name}'.")
            except IndexError:
                voice_io.show("Playback failed : Sorry, but the entered number is not within the range of available options.")
                    
            except SyntaxError or TypeError:
                voice_io.show("Playback failed : Sorry, but your entered data is not a number.") 
        
        else:
            voice_io.show(f"Sorry, could not find any audio file with the name '{name}'")

    else:
        voice_io.show(f"Sorry, could not find any audio file with the name '{name}'")
