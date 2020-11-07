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
            voice_io.show("Hold on! \nMultiple file deletion is still being worked on!")
    else:
        voice_io.show(f"File {file_name} was not found, please check if the file you named exists or\nhas been spelled correctly.")


def deleteFolder(folder_name, search_dir):
    folder_search_results = folderSearch(folder_name, search_dir)
    if folder_search_results != []:
        if len(folder_search_results) == 1:
            invoice.inpt("%s from %s will be permanently lost, press Enter to continue."%(folder_search_results[0]["folder"]), folder_search_results[0]["root"], iterate = False)
            os.rmdir(folder_search_results[0]["root"] + "/" + folder_search_results[0]["folder"])
            voice_io.show(folder_name,"has been deleted successfully!")
            
        else:
            voice_io.show("Hold on! \nMultiple folder deletion is still being worked on!")
    else:
        voice_io.show(f"Folder {folder_name} was not found, please check if the folder you named exists or\nhas been spelled correctly")

def copy(obj_name, search_dir, dest_dir):
    dest_dir = get_dirs.HOME + "/" + dest_dir
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)

    folder_search_results = folderSearch(obj_name, search_dir)
    file_search_results = fileSearch(obj_name, search_dir)
    if folder_search_results != []:
        if len(folder_search_results) == 1:
            #invoice.inpt(f"Copying folder {folder_search_results[0]["folder"]} from {folder_search_results[0]["root"]} to {dest_dir}.....")
            shutil.copy2()
    
    elif file_search_results != []:
        pass
        


def rname(self):
    pass

def move(self):
    pass

def createFile(self):
    pass

def createFolder(self):
    pass