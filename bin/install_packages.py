import importlib.util
import sys
import os
import subprocess as sub

def setup():
    commands = {
        "gtts": "pip3 install gTTS",
        "playsound": "pip3 install playsound",
        "pyttsx3": "pip3 install pyttsx3",
        "pyaudio": "pip3 install PyAudio-0.2.11-cp39-cp39-win_amd64.whl",
        "speech_recognition": "pip3 install SpeechRecognition",
        "bs4": "pip3 install bs4"
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
            sub.check_output(commands[name], shell = True)
    return True