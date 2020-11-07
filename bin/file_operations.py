#file operations go here! 
#file handler
from importlib.abc import FileLoader
import os
import shutil

from bin import get_dirs
from bin import voice_io
from bin import invoice

folder_search_results = []

def fileSearch(file_name, search_dir):
#Searches for the given file name in the file tree(case sensitive)
    file_search_results = []
    for root, dirs, files in os.walk(search_dir): 
        for file in files:
            if file_name in file:  
                file_search_results.append({"root": root, "file": file})

    return  file_search_results
    
def folderSearch(folder_name, search_dir):
#Searches for the given folder name in the file tree(case sensitive)
    for root, dirs, files in os.walk(search_dir): 
        for folder in dirs:
            if  folder_name in folder:  
                folder_search_results.append({"root": root, "folder": folder})

    return  folder_search_results == []
    
def deleteFile(file_name,search_dir):
    file_search_results = fileSearch(file_name, search_dir)
    if file_search_results != []:
        if len(file_search_results) == 1:
            invoice.inpt("%s from %s will be permanently lost, press Enter to continue."%(file_search_results[0]["file"], file_search_results[0]["root"]), iterate = False)
            os.remove(file_search_results[0]["root"] + "/" + file_name)
            voice_io.show(file_name," has been deleted successfully!")
            
        else:
            voice_io.show("Hold on! \nMultiple file deletion is still being worked on!")
    else:
        voice_io.show(f"File {file_name} was not found, please check if the file you named exists or\nhas been spelled correctly.")


def deleteFolder(folder_name):
    if folderSearch():
        if len(folder_search_results) == 1:
            invoice.inpt("%s from %s will be permanently lost, press Enter to continue."%(folder_search_results[0]["folder"]), folder_search_results[0]["root"], iterate = False)
            os.rmdir(folder_search_results[0]["root"] + folder_name)
            voice_io.show(folder_name,"has been deleted successfully!")
            
        else:
            voice_io.show("Hold on! \nMultiple folder deletion is still being worked on!")
    else:
        voice_io.show(f"Folder {folder_name} was not found, please check if the folder you named exists or\nhas been spelled correctly")

def copy(obj_name):
    pass



def rname(self):
    pass

def move(self):
    pass

def createFile(self):
    pass

def createFolder(self):
    pass