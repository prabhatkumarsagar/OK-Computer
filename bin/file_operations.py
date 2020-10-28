#file operations go here! 
#file handler
import os
import shutil

class File_Handler:

    def __init__(self, operation, file_name = "", folder_name = ""):
        self.operation = operation
        self.file_name = file_name
        self.folder_name = folder_name
        self.search_dir = ""
        self.file_search_results = []
        self.folder_search_results = []

    def getDir(self):
        file_name = self.file_name
        if os.name == 'nt':
            home = os.environ['USERPROFILE']
        
        elif os.name == 'posix':
            home = os.getenv("HOME")

        print("Search where?\n1. Desktop\n2. Downloads\n3. Documents\n4. Music\n5. Pictures\n6. Videos\n7. Entire home directory")
        ch = int(input("Enter your choice here : "))

        if ch == 1:
            print("Searching in Desktop")
            self.search_dir = home + "/Desktop"
        if ch == 2:
            print("Searching in Downloads")
            self.search_dir = home + "/Downloads"
        if ch == 3:
            print("Searching in Documents")
            self.search_dir = home + "/Documents"
        if ch == 4:
            print("Searching in Music")
            self.search_dir = home + "/Music"
        if ch == 5:
            print("Searching in Pictures")
            self.search_dir = home + "/Pictures"
        if ch == 6:
            print("Searching in Videos")
            self.search_dir = home + "/Videos"
        if ch == 7:
            print("Searching in Home")
            self.search_dir = home
        return
    def fileSearch(self):
        #Searches for the given file name in the file tree(case sensitive)
        for root, dirs, files in os.walk(self.search_dir): 
            for file in files:
                if self.file_name in file:  
                    self.file_search_results.append({"root": root, "file": file})

        return self.file_search_results == []
    
    def folderSearch(self):
        #Searches for the given folder name in the file tree(case sensitive)
        for root, dirs, files in os.walk(self.search_dir): 
            for folder in dirs:
                if self.folder_name in folder:  
                    self.folder_search_results.append({"root": root, "folder": folder})

        return self.folder_search_results == []
    
    def deleteFile(self):
        if len(self.file_search_results) == 1:
            confirmation = confirm("%s from %s will be permanently lost, do you want to continue?"%(self.file_search_results[0]["file"]),self.file_search_results[0]["root"]))
            os.remove(self.file_name)
            message(file_name,"has been deleted successfully!")
        
        else:
            msg

    def deleteFolder(self):
        os.remove(self.folder_name)
        message(self.folder_name,"has been deleted successfully!")

    def copy(self):


    def rname(self):

    def move(self):

    def createFile(self):

    def createFolder(self):

    def main(self):
        op = self.operation
        self.getDir()

        if not self.fileSearch() or not self.folderSearch():
            message("Oops! The file/folder name that you entered seem to be missing. Please make sure that the file/folder you are trying to operate on exists or if the name has been spelled correctly and try again!")
            return
        
        else:
            if op == "del_file":
                self.deleteFile()
                return

            if op == "del_folder":
                self.deleteFolder()
                return

            if op == "rname_file":
                self.rname()
                return

            if op == "copy_file":
                self.copy()
                return

            if op == "move_file":
                self.move()
                return
        
            if op == "create file":
                self.createFile()
                return
    
            if op == "create folder":
                self.createFolder()
                return