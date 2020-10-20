#file operations go here!

#file handler
import os
import shutil

class File_Handler:
    operation = []

    

    def __init__(self, operation, file_name):
        self.operation = operation
        self.file_name = file_name

    def fileSearch(self, search_type, search_path):
        file_name = self.file_name
        if os.name == 'nt':
            home = os.environ['USERPROFILE']
        
        elif os.name == 'posix':
            home = os.getenv("HOME")

        print("Search where?\n1. Desktop\n2. Downloads\n3. Documents\n4. Music\n5. Pictures\n6. Videos\n7. Entire home directory")
        ch = int(input("Enter your choice here : "))
        if ch == 1:
            print("Searching in Desktop")
            search_dir = home + "/Desktop"
        if ch == 2:
            print("Searching in Downloads")
            search_dir = home + "/Downloads"
        if ch == 3:
            print("Searching in Documents")
            search_dir = home + "/Documents"
        if ch == 4:
            print("Searching in Music")
            search_dir = home + "/Music"
        if ch == 5:
            print("Searching in Pictures")
            search_dir = home + "/Pictures"
        if ch == 6:
            print("Searching in Videos")
            search_dir = home + "/Videos"
        if ch == 7:
            print("Searching in Home")
            search_dir = home

        for root, dirs, files in os.walk(search_dir): 
            if file_name in files:  
                return root, dirs, files
        return False
    
    def delete_file(self):
        if not self.search():
            message("Oops! The file name that you entered seem to be missing. Please make sure that the file you are trying to delete exists or if the name has been spelled correctly and try again!")
        
        else:
            os.remove(self.file_name)
            message(file_name,"has been deleted successfully!")
        
    def copy(self):

    def rname(self):

    def move(self):

    def createFile(self):

    def createFolder(self):

    def main(self):
        op = self.operation
        if op == "del":
            self.delete()
            return

        if op == "rname":
            self.rname()
            return

        if op == "copy":
            self.copy()
            return

        if op == "move":
            self.move()
            return
        
        if op == "create file":
            self.createFile()
            return
    
        if op == "create folder":
            self.createFolder()
            return
        

        