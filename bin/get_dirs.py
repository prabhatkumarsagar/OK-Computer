import os

if os.name == 'nt':
	HOME =  os.environ['USERPROFILE']
        
elif os.name == 'posix':
	HOME = os.getenv("HOME")

#important user directories

DESKTOP =  HOME + "/Desktop"
DOWNLOADS = HOME + "/Downloads"
DOCUMENTS = HOME + "/Documents"
MUSIC = HOME + "/Music"
PICTURES = HOME + "/Pictures"
VIDEOS = HOME + "/Videos"

#Assistant data directories
PATH_USR_DATA = HOME + "/Documents/python_assistant_userdata/"
FILE_USR_DATA = HOME + "/Documents/python_assistant_userdata/user_info.dat"