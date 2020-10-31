import os

def clear():
    if os.name == "nt":
        os.system("clr")

    else:
        os.system("clear")