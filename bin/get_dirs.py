import os

if os.name == 'nt':
	HOME =  os.environ['USERPROFILE']
        
elif os.name == 'posix':
	HOME = os.getenv("HOME")
	
PATH_USR_DATA = HOME + "/Documents/python_assistant_userdata/"
FILE_USR_DATA = HOME + "/Documents/python_assistant_userdata/user_info.dat"
