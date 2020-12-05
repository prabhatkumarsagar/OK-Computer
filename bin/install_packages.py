import importlib.util
import sys
import os
import subprocess

def install():
    commands = {
        "gtts": "pip3 install gTTS",
        "playsound": "pip3 install playsound",
        "pyttsx3": "pip3 install pyttsx3",
        "pyaudio": "pip3 install PyAudio-0.2.11-cp39-cp39-win_amd64.whl",
        "speech_recognition": "pip3 install SpeechRecognition",
        "bs4": "pip3 install bs4",
        "wolframalpha": "pip3 install wolframalpha",
        "wikipedia": "pip3 install wikipedia",
        'mysql': "pip3 install mysql-connector-python",
        "pyowm": "pip3 install pyowm",
        "geocoder": "pip3 install geocoder",
        "cryptography": "pip3 install cryptography",
        "lxml": "pip3 install lxml"
    }
    # bs4 is a dependency for gtts
    #pyaudio is a dependency for speech_recognition
    for name in commands.keys():
        if name in sys.modules:
            pass
        elif (spec := importlib.util.find_spec(name)) is not None:
            pass
        else:
            if name == "pyaudio":
                if os.name == "posix":
                    print("Your system is missing the python package PyAudio which is required by this program for voice functions.")
                    print("Please install 'python3-pyaudio' manually from your distro repos and run this program again.")
                    return False
            try:
                subprocess.check_output(commands[name], shell = True)
            except subprocess.CalledProcessError:
                if os.name == "nt":
                    print("Installation of required packages failed!\nPIP has not been installed in your system. To install pip, please \nre-run the python setup process and make sure to check the 'Install PIP' check box!")
                
                else :
                    print("PIP3 is not installed in your system! \nPlease install python3-pip from your distro repos and run this app again!")
                
                return False

            except pip._vendor.urllib3.exceptions.ReadTimeoutError or socket.timeout:
                print("Unable to download the required packages.\nTry connecting to the internet or using a faster connection.")
                return False
                
    return True