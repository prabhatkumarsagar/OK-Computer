import os

from bin import get_home

path_user_data = get_home.PATH_USR_DATA
print(path_user_data)

import pickle as pk

if os.exists(path_user_data):
    usr_data = open(path_user_data)
    try: