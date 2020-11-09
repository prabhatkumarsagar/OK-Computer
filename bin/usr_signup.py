import pickle as pk
import os
import getpass

from bin import get_dirs
from bin import clear
from bin import voice_io
from bin import invoice

voice = True

def setNewUser():
    usr_info_dic={}
    clear.clear()
    os.mkdir(get_dirs.PATH_USR_DATA)
    voice_io.show("What shall i call you? ", sound = voice)
    nm = invoice.inpt() #Name of the user i.e the name by which the assistant will call him/her
    voice_io.show("And you are, Master or Miss, master? ", sound = voice) #Gender of the user which the assistant will refer to again and again
    gnd = invoice.inpt()
    voice_io.show("Now What would be your email? (incase i run into some errors and you feel like reporting and blah blah) ", sound = voice)#usr email address
    eml = invoice.inpt()
    pswd = getpass.getpass(voice_io.show("And lastly please set up a password (incase you want to tweak stuff around later on you'll be needing this) ",show_output = False, sound = voice))#use password

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
#print(usr_info_dic)

def info_in(x):
    f=open(get_dirs.FILE_USR_DATA,'wb')
    pk.dump(x,f)
    f.close()


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
            try:
                r=pk.load(f1)
                r[u]=x
                pk.dump(r,f2)
            except:
                break
        f1.close()
        f2.close()
        os.remove("usr_info.dat")
        os.rename("usr_info1.dat","usr_info.dat")
        f=open("./usr_info.dat","rb+")
        rd=pk.load(f)
        print(rd)
        f.close()

def info_update():
    global u
    while True:
        print("What do you wanna Update?")
        print("1. Name")
        print("2. Gender")
        print("3. Email")
        print("4. Password")
        print("5. All")
        print("6. NOTHING; EXIT PLEASE")
        ch=input("What entry do you want to update? ")
        if ch=='1':
            u='name'
            in_upd_entr()
        elif ch=='2':
            u='gender'
            in_upd_entr()
        elif ch=='3':
            u='email'
            in_upd_entr()
        elif ch=='4':
            u='password'
            in_upd_entr()
        elif ch=='5':
            print("Sorry but i currently cannot update all the values at once! please try doing it separately!")
            break
        elif ch=='6':
            break
        else:
            print("Invalid Input!")
            break
        in_upd_entr()  

def main(**kwargs):
    global sound

    if kwargs["operation"] == "new":
        sound = kwargs["sound"]
        setNewUser()
        print(sound)
    
    elif kwargs["operation"] == "fetch":
        return info_out(kwargs["data_type"])

    elif kwargs["operation"] == "update":
        info_update()

#setNewUser()