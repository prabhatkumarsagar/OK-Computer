import os

from bin import get_home
from bin import usr_signup

path_user_data = get_home.PATH_USR_DATA
#print(path_user_data)

import pickle as pk

#this portion is dedicated to new-user sign-up
if os.exists(path_user_data):
    #usr_data = open(path_user_data)
    pass

else:
    os


