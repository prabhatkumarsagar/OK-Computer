import pickle as pk
import os
import getpass
import webbrowser
#from bin import get_dirs
#from bin import clear
#from bin import voice_io
#from bin import invoice
import get_dirs
import clear
import voice_io
import invoice
sound = False
#sound = True

def setNewUser():
    usr_info_dic={}
    clear.clear()
    voice_io.show("What shall i call you Master? ", sound = sound)
    nm = invoice.inpt() #Name of the user i.e the name by which the assistant will call him/her
    voice_io.show("\nAnd you are, Master or Miss, master? ", sound = sound) #Gender of the user which the assistant will refer to again and again
    gnd = invoice.inpt()
    voice_io.show("\nNow What would be your email address? I will be needing this for my email operations so that i can help you with sending automated emails to others without you lifting a finger and also for helping you send feedback to my developers regarding bugs or minor issues, which i would hope doesn't happen :D", sound = sound)#usr email address
    eml = invoice.inpt()
    pswd = getpass.getpass(voice_io.show("\nAnd lastly what is your email password? Note: All these personal information is stored only and only on your local machine and hence there's no way i can compromise your data, In short you can trust me ;) ",show_output = False, sound = sound) + "\nPassword: ")#use password
    voice_io.show("\nRegarding email operations, please note that for properly executing them you will have to make sure to turn on \"Less Secure Apps\" for your google account. \n\nWhich if you want to do now, please enter 'YES' and a webpage will be prompted with an option to turn on \"Less Secure Apps\" for your google account right away and just by clicking on that the program will be good to go! Otherwise enter 'NO' and you can always do it later in assistant settings.", sound = sound)
    ch = invoice.inpt()

    if ch.lower()=="yes":
        print("Okay! Here you go!")
        webbrowser.open("https://myaccount.google.com/lesssecureapps?")
    elif ch.lower()=="no" or ch.lower()=="":
        print("Alright!")
    
    usr_info_dic['name']=nm
    GND_FEMALE=["girl",'miss','missus','mrs','female','lady','woman']
    GND_MALE=["boy","master","mister","mr","male","lodu","man"]

    if gnd.lower() in GND_FEMALE:
        usr_info_dic['gender']="Female"
    elif gnd.lower() in GND_MALE:
        usr_info_dic['gender']="Male"
    else:   
        usr_info_dic['gender']="Others"

    usr_info_dic['email']=eml
    usr_info_dic['password']=pswd
    info_in(usr_info_dic)
    print(usr_info_dic)
    exit()

def info_in(x):
    f1=open("./usr_info.dat",'wb+')
    f2=open(get_dirs.FILE_USR_DATA,'wb+')
    pk.dump(x,f1)
    pk.dump(x,f2)
    f1.close()
    f2.close()


def info_out(x="all"):
    f=open(get_dirs.FILE_USR_DATA,'rb+')
    rd=pk.load(f)
    ch=x.lower()
    if ch=="name":
        return rd[ch]
        f.close()

    elif ch=="gender":
        return rd[ch]
        f.close()

    elif ch=="email":
        return rd[ch]
        f.close()

    elif ch=="password":
        return rd[ch]
        f.close()

    elif ch=="all":
        return rd
        f.close()

    else:
        return False
        f.close()


u=''

def in_upd_entr():
    global u
    f1=open("./usr_info.dat","rb+")
    f2=open("./usr_info1.dat","wb+")
    x=input("Enter new value: ")
    while True:
        r=pk.load(f1)
        r[u]=x
        pk.dump(r,f2)
        #f2.flush()
        break
    f1.close()
    f2.close()
    os.remove("usr_info.dat")
    os.rename("usr_info1.dat","usr_info.dat")
    f=open("./usr_info.dat","rb+")
    rd=pk.load(f)
    f3=open(get_dirs.FILE_USR_DATA,'wb+')
    pk.dump(rd,f3)
    f3.close()
    f.close()

def info_update():
    global u
    while True:
        print("What do you wanna Update?")
        print("1. Name")
        print("2. Gender")
        print("3. Email")
        print("4. Password")
        print("5. Nothing (Exit)")
        ch=input("What entry do you want to update? ")
        if ch=='1':
            u='name'
            in_upd_entr()
            break
        elif ch=='2':
            u='gender'
            in_upd_entr()
            break
        elif ch=='3':
            u='email'
            in_upd_entr()
            break
        elif ch=='4':
            u='password'
            in_upd_entr()
            break
        elif ch=='5':
            return
        else:
            print("Invalid Input!")
            return
    print("Data Updated Successfully!")

def main(**kwargs):
    global sound

    if kwargs["operation"] == "new":
        sound = kwargs["sound"]
        setNewUser()
    
    elif kwargs["operation"] == "fetch":
        return info_out(kwargs["data_type"])

    elif kwargs["operation"] == "update":
        info_update()

#setNewUser()
#print(info_out("all"))
#info_update()
