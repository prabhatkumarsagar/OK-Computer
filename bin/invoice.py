from bin import clear
from bin import usr_signup

def inpt(text = ">>>", sound = False, audio_io = True, iterate = True):
    usr_name = usr_signup.main(operation = "fetch", data_type = "name")
    if audio_io:
        from bin import voice_io
        
        while True:
            try:
                entered_data = input(text)
                #print("input = ",entered_data)
                
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
                                voice_io.show("\nSorry, could not get that! Please try again..\n", sound = sound)
                    
                        except KeyboardInterrupt:#stops voice input when ctrl+c is pressed 
                            voice_io.show("\nStopped listening", sound = sound)
                            entered_data = ""
                            voice_data = True

                elif entered_data == "":
                    if not iterate:
                        break
                    continue

                elif "clear" in entered_data.lower() or entered_data.lower() in "clrcls":
                    clear.clear()
                    voice_io.show(f"""Hey {usr_name}! 
        
What would you like me to do?""", sound = sound)


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