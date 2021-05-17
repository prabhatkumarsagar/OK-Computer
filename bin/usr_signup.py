import pickle as pk
import os
import getpass
from platform import processor
import webbrowser
import base64
import bcrypt
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from bin import get_dirs
from bin import clear
from bin import voice_io
from bin import invoice
#import get_dirs
#import clear
#import voice_io
#import invoice
#sound = True

key = ""
def setNewUser():
    usr_info_dic={}
    clear.clear()
    voice_io.show("What shall I call you Master? ")
    nm = bytes(invoice.inpt(), encoding = "utf-8") #Name of the user i.e the name by which the assistant will call him/her
    voice_io.show("\nAnd you are, Master or Miss, master? ") #Gender of the user which the assistant will refer to again and again
    gnd = invoice.inpt()
    asst_pswd = bytes(getpass.getpass(voice_io.show("\nWhat should be your password for accessing me?",show_output = False) + "\nPassword: "), encoding = "utf-8")#
    salt = b'$2b$12$3hbla5Xs2Ekx9SGVYfWQuO'
    hashed_pswd = bcrypt.hashpw(asst_pswd, salt)
    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                    )
    global key
    key = base64.urlsafe_b64encode(kdf.derive(hashed_pswd))

    voice_io.show("\nNow What would be your email address? \nI will be needing this for my email operations so that i can help you with sending automated emails to others without you lifting a finger and also for helping you send feedback to my developers regarding bugs or minor issues, which i would hope doesn't happen :D")#usr email address
    eml = bytes(invoice.inpt(processed= False), encoding = "utf-8")

    pswd = bytes(getpass.getpass(voice_io.show("\nAnd lastly what is your email password? Note: All these personal information is stored only and only on your local machine and hence there's no way i can compromise your data, In short you can trust me ;) ",show_output = False) + "\nPassword: "), encoding = "utf-8")#use password
    voice_io.show("\nRegarding email operations, please note that for properly executing them you will have to make sure to turn on \"Less Secure Apps\" for your google account. \n\nWhich if you want to do now, please enter 'YES' and a webpage will be prompted with an option to turn on \"Less Secure Apps\" for your google account right away and just by clicking on that the program will be good to go! Otherwise enter 'NO' and you can always do it later in assistant settings.")
    ch = invoice.inpt()
    if ch.lower()=="yes":
        voice_io.show("Okay! Here you go!")
        webbrowser.open("https://myaccount.google.com/lesssecureapps?")
    elif ch.lower()=="no" or ch.lower()=="":
        voice_io.show("Alright!")
            
    cipher_suite = Fernet(key)
    usr_info_dic['name']=cipher_suite.encrypt(nm)
    GND_FEMALE=["girl",'miss','missus','mrs','female','lady','woman']
    GND_MALE=["boy","master","mister","mr","male","lodu","man"]

    if gnd.lower() in GND_FEMALE:
        usr_info_dic['gender']=cipher_suite.encrypt(b"Female")
    elif gnd.lower() in GND_MALE:
        usr_info_dic['gender']=cipher_suite.encrypt(b"Male")
    else:   
        usr_info_dic['gender']=cipher_suite.encrypt(b"Others")
    usr_info_dic["asst_password"] = cipher_suite.encrypt(hashed_pswd)
    usr_info_dic['email']=cipher_suite.encrypt(eml)
    usr_info_dic['password']=cipher_suite.encrypt(pswd)
    info_in(usr_info_dic)
    voice_io.show("Well then now you're good to go! Just press Enter/Return to get going!", end = "")
    invoice.inpt("", iterate = False)
    return key, str(nm)

def info_in(x):
    #f1=open("./usr_info.dat",'wb+')
    f2=open(get_dirs.FILE_USR_DATA,'wb+')
    #pk.dump(x,f1)
    pk.dump(x,f2)
    #f1.close()
    f2.close()


def info_out(key, x="all"):
    f=open(get_dirs.FILE_USR_DATA,'rb+')
    cipher_suite = Fernet(key)
    rd=pk.load(f)
    ch=x.lower()
    f.close()
    if ch=="name":
        name = ""
        try:
            name = bytes(cipher_suite.decrypt(rd[ch])).decode("utf-8")
            return name
        
        except:
            return False
        

    elif ch=="gender":
        return bytes(cipher_suite.decrypt(rd[ch])).decode("utf-8")
        f.close()

    elif ch=="email":
        return bytes(cipher_suite.decrypt(rd[ch])).decode("utf-8")
        f.close()

    elif ch=="password":
        return bytes(cipher_suite.decrypt(rd[ch])).decode("utf-8")
        f.close()

    elif ch == "mysql_usr":
        return bytes(cipher_suite.decrypt(rd[ch])).decode("utf-8")
        f.close()
    
    elif ch == "mysql_pswd":
        return bytes(cipher_suite.decrypt(rd[ch])).decode("utf-8")
        f.close()

    elif ch=="all":
        nrd = {}
        for i in rd.keys():
            nrd[i] = bytes(cipher_suite.decrypt(rd[i])).decode("utf-8")
        return nrd
        f.close()

    else:
        return False
        f.close()


u=''

def in_upd_entr(key):
    global u
    usr_info1 = get_dirs.FILE_USR_DATA
    usr_info2 = get_dirs.PATH_USR_DATA + "/user_info1.dat"
    f1=open(usr_info1,"rb+")
    f2=open(usr_info2,"wb+")
    x=input("Enter new value : ")
    while True:
        r=pk.load(f1)
        r[u]=x
        pk.dump(r,f2)
        #f2.flush()
        break
    f1.close()
    f2.close()
    os.remove(usr_info2)
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
        voice_io.show("What do you wanna Update?")
        voice_io.show("1. Name")
        voice_io.show("2. Gender")
        voice_io.show("3. Email")
        voice_io.show("4. Password")
        voice_io.show("5. Nothing (Exit)")
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
            voice_io.show("Invalid Input!")
            return
    voice_io.show("Data Updated Successfully!")

def main(**kwargs):
    if kwargs["operation"] == "new":
        return setNewUser()
    
    elif kwargs["operation"] == "fetch":
        return info_out(kwargs["key"], kwargs["data_type"])

    elif kwargs["operation"] == "update":
        info_update(kwargs["key"])

#setNewUser()
# voice_io.show(info_out("all"))
#info_update()
