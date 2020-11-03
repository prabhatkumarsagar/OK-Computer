import importlib.util
import sys
import subprocess as sub

def setup():
    commands = {
        "gtts": "pip3 install gTTS",
        "playsound": "pip3 install playsound",
        "pyttsx3": "pip3 install pyttsx3",
        "pyaudio": "pip3 install PyAudio-0.2.11-cp39-cp39-win_amd64.whl",
        "speech_recognition": "pip3 install SpeechRecognition"
    }
    # For illustrative purposes.
    for name in commands.keys():

        if name in sys.modules:
            pass
        elif (spec := importlib.util.find_spec(name)) is not None:
            pass
        else:
            sub.check_output(commands[name], shell = True)
    return True