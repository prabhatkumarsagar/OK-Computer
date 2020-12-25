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
FILE_ASSISTANT_SETTINGS = PATH_USR_DATA + "assistant_settings.dat"
FILE_SOUND_VALUE = PATH_USR_DATA + 'ass_sound_val.dat'
FILE_USR_DATA = HOME + "/Documents/python_assistant_userdata/user_info.dat"
FILE_ENCRYPT_KEY = PATH_USR_DATA + "key.bin"
DB_NOTES_REMINDERS = PATH_USR_DATA + "notes_reminders.db"