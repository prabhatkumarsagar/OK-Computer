import os
import pickle as pk

from bin import get_dirs
from bin import usr_signup
from bin import clear

file_user_data = get_dirs.FILE_USR_DATA
#print(path_user_data)

def main():
    #this portion is dedicated to new-user sign-up
    if os.path.exists(file_user_data):
        #usr_data = open(path_user_data)
        pass

    else:
        userSetup()

    
def userSetup():
    if not os.path.exists(get_dirs.PATH_USR_DATA):
        os.mkdir(get_dirs.PATH_USR_DATA)
    usr_signup.main(operation = "new")

main()