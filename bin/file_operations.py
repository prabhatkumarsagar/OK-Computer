#file operations go here! 
#file handler
from importlib.abc import FileLoader
import os
import shutil

from bin import get_dirs
from bin import voice_io
from bin import invoice

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
                voice_io.show("Deletion failed : Sorry, but the entered number was within the range of available options.")
            
            except SyntaxError or TypeError:
                voice_io.show("Deletion failed : Sorry, but your entered data was not a number.")

    else:
        voice_io.show(f"Could not find file '{file_name}', please check if the file you named exists or\nhas been spelled correctly.")


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
                voice_io.show("Deletion failed : Sorry, but the entered number was within the range of available options.")
            
            except SyntaxError or TypeError:
                voice_io.show("Deletion failed : Sorry, but your entered data was not a number.")

    else:
        voice_io.show(f"Could not find file '{folder_name}', please check if the file you named exists or\nhas been spelled correctly.")

def copy(obj_name, search_dir, dest_dir):
    dest_dir = get_dirs.HOME + "/" + dest_dir
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)

    folder_search_results = folderSearch(obj_name, search_dir)
    file_search_results = fileSearch(obj_name, search_dir)
    if folder_search_results != []:
        if len(folder_search_results) == 1:
            voice_io.show(f'Copying folder {folder_search_results[0]["folder"]} from {folder_search_results[0]["root"]} to {dest_dir}.....')
            shutil.copy2(folder_search_results[0]["root"] + "/" + folder_search_results[0]["folder"], dest_dir)
        
        else:
            voice_io.show("Hold on! \nMultiple folder copying is still being worked on!")
        
    
    elif file_search_results != []:
        if len(file_search_results) == 1:
            voice_io.show(f'Copying folder {file_search_results[0]["file"]} from {file_search_results[0]["root"]} to {dest_dir}.....')
            shutil.copy2(file_search_results[0]["root"] + "/" + file_search_results[0]["file"], dest_dir)

        else:
            voice_io.show("Hold on! \nMultiple file copying is still being worked on!")

    else:
        voice_io.show("Given file/folder {obj_name} was not found!")

def rname(obj_name, new_name, search_dir):
    folder_search_results = folderSearch(obj_name, search_dir)
    file_search_results = fileSearch(obj_name, search_dir)
    if file_search_results != [] and folder_search_results != []:
        if len(folder_search_results) == 1 and len(file_search_results) == 1:
            voice_io.show(f' folder {folder_search_results[0]["folder"]} from {folder_search_results[0]["root"]} to {dest_dir}.....')
            os.rename(folder_search_results[0]["root"] + "/" + folder_search_results[0]["folder"], folder_search_results[0]["root"] + "/" + new_name)
        
        else:
            voice_io.show("Hold on! \nMultiple folder copying is still being worked on!")
        
    if folder_search_results != []:
        if len(folder_search_results) == 1:
            voice_io.show(f' folder {folder_search_results[0]["folder"]} from {folder_search_results[0]["root"]} to {dest_dir}.....')
            shutil.copy2(folder_search_results[0]["root"] + "/" + folder_search_results[0]["folder"], dest_dir)
        
        else:
            voice_io.show("Hold on! \nMultiple folder copying is still being worked on!")
        
    
    elif file_search_results != []:
        if len(file_search_results) == 1:
            voice_io.show(f'Copying folder {file_search_results[0]["file"]} from {file_search_results[0]["root"]} to {dest_dir}.....')
            shutil.copy2(file_search_results[0]["root"] + "/" + file_search_results[0]["file"], dest_dir)

        else:
            voice_io.show("Hold on! \nMultiple file copying is still being worked on!")

    else:
        voice_io.show("Given file/folder {obj_name} was not found!")

def createFile(self):
    pass

def createFolder(self):
    pass