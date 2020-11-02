from bin import clear
from bin import voice_io

def inpt(text = "", voice = False):
    try:
        text = ">>>" + text
        entered_data = input(text)
        
        if entered_data == "voice":
            i = 0
            voice_data = False
            while not voice_data:
                try:
                    print(voice)
                    voice_io.show("I am listening......", voice = voice)
                    voice_data = entered_data = voice_io.voice_in()
                    print(voice_data)
                    i += 1
                    if i >= 1:
                        voice_io.show("\nSorry, could not get that! Please try again..\n", voice = voice)
            
                except KeyboardInterrupt:#stops voice input when ctrl+c is pressed 
                    voice_io.show("\nStopped listening", voice = voice)
                    entered_data = ""
                    voice_data = True
    
        elif "clear" in entered_data.lower() or entered_data.lower() == "clrcls":
            print("hello1")
            #clear.clear()

        elif entered_data.lower() in "exitquitend":
            voice_io.show("\n\nBye and have a nice day!", voice = voice)
            exit()
        else:        
            return entered_data
    #except KeyboardInterrupt:#exits from the program when ctrl+c is pressed
        voice_io.show("Do you really want to exit?(Yes to confirm, any other input to deny).", voice = voice)
        ch = input(">>>")
        if ch == "Yes":
            voice_io.show("\n\nBye and have a nice day!", voice = voice)
            exit()
