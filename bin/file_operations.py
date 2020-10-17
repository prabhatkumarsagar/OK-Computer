#file operations go here!

#file handler
import os

class File_Handler:
    operation = []

    def __init__(self, operation, ):
        self.operation = operation

    def fileSearch(self):

    
    
    def delete(self):

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
        
        