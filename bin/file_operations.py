#file operations go here! 
#file handler
import os
import shutil

from bin import get_dirs
from bin import voice_io

file_search_results = []
folder_search_results = []


def fileSearch(file_name, search_dir):
#Searches for the given file name in the file tree(case sensitive)
    for root, dirs, files in os.walk(search_dir): 
        for file in files:
            if file_name in file:  
                file_search_results.append({"root": root, "file": file})

    return  file_search_results == []
    
def folderSearch(folder_name, search_dir):
#Searches for the given folder name in the file tree(case sensitive)
    for root, dirs, files in os.walk( search_dir): 
        for folder in dirs:
            if  folder_name in folder:  
                folder_search_results.append({"root": root, "folder": folder})

    return  folder_search_results == []
    
def deleteFile(self):
    if len( file_search_results) == 1:
        confirmation = confirm("%s from %s will be permanently lost, do you want to continue?"%( file_search_results[0]["file"]), file_search_results[0]["root"])
        os.remove( file_name)
        message(file_name,"has been deleted successfully!")
        
    else:
        msg

def deleteFolder(self):
    os.remove( folder_name)
    message( folder_name,"has been deleted successfully!")

def copy(self):


def rname(self):

def move(self):

def createFile(self):

def createFolder(self):
