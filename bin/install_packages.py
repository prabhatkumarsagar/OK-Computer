import importlib.util
import sys
import os
import subprocess

def install():
    commands = {
        "gtts": "pip3 install gTTS --user",
        "playsound": "pip3 install playsound --user",
        "pyttsx3": "pip3 install pyttsx3 --user",
        "speech_recognition": "pip3 install SpeechRecognition --user",
        "bs4": "pip3 install bs4 --user",
        "wolframalpha": "pip3 install wolframalpha --user",
        "wikipedia": "pip3 install wikipedia --user",
        "pyaudio": "pipwin install https://download.lfd.uci.edu/pythonlibs/z4tqcw5k/PyAudio-0.2.11-cp39-cp39-win_amd64.whl --user",
        "pyowm": "pip3 install pyowm --user",
        "geocoder": "pip3 install geocoder --user",
        "cryptography": "pip3 install cryptography --user",
        "lxml": "pip3 install lxml --user",
        "tabulate": "pip3 install tabulate --user"
    }
    # bs4 is a dependency for gtts
    #pyaudio is a dependency for speech_recognition
    for name in commands.keys():
        if name in sys.modules:
            pass
        elif (spec := importlib.util.find_spec(name)) is not None:
            pass
        else:
            if name == "pipwin" and os.name != "nt":
                continue

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