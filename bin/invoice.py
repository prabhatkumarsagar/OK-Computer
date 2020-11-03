from bin import clear
from bin import voice_io

def inpt(text = ">>>", sound = False, audio_io = True):
    if audio_io:
        try:
            entered_data = input(text)
            print("input = ",entered_data)
            
            if entered_data == "voice":
                i = 0
                voice_data = False
                while not voice_data:
                    try:
                        voice_io.show("I am listening......", sound = sound)
                        voice_data = entered_data = voice_io.voice_in()
                        print(voice_data)
                        i += 1
                        if i >= 1:
                            voice_io.show("\nSorry, could not get that! Please try again..\n", voice = voice)
                
                    except KeyboardInterrupt:#stops voice input when ctrl+c is pressed 
                        voice_io.show("\nStopped listening", sound = sound)
                        entered_data = ""
                        voice_data = True

            elif entered_data == "":
                return
        
            elif "clear" in entered_data.lower() or entered_data.lower() == "clrcls":
                print("hello1")
                #clear.clear()

            elif entered_data.lower() in "exitquitend":
                print(entered_data.lower() in "exitquitend")
                voice_io.show("\n\nBye and have a nice day!", sound = sound)
                exit()

            else:        
                return entered_data

        except KeyboardInterrupt:#exits from the program when ctrl+c is pressed
            voice_io.show("\n\nBye and have a nice day!", sound = sound)
            exit()
        
    else:
        input(text)
        return
