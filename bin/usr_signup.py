import pickle as pk
import os
usr_info_dic={}

nm=input("What shall i call you? ") #Name of the user i.e the name by which the assistant will call him/her
gnd=input("And you are, Master or Miss, master? ") #Gender of the user which the assistant will refer to again and again
eml=input("Now What would be your email? (incase i run into some errors and you feel like reporting and blah blah) ")
pswd=input("And lastly please set up a password (incase you want to tweak stuff around later on you'll be needing this) ")
usr_info_dic['name']=nm
gnd1=["girl",'miss','missus','mrs','female','lady','woman']
gnd2=["boy","master","mister","mr","male","lodu","man"]
if gnd.lower() in gnd1:
    usr_info_dic['gender']="Female"
elif gnd.lower() in gnd2:
    usr_info_dic['gender']="Male"
else:
    usr_info_dic['gender']="Others"
usr_info_dic['email']=eml
usr_info_dic['password']=pswd
#print(usr_info_dic)

def info_in(x):
    f=open("./usr_info.dat",'wb')
    pk.dump(x,f)
    f.close()

info_in(usr_info_dic)


def info_out(x="all"):
    f=open("./usr_info.dat",'rb+')
    rd=pk.load(f)
    ch=x.lower()
    if ch=="name":
        print(rd[ch])
    elif ch=="gender":
        print(rd[ch])
    elif ch=="email":
        print(rd[ch])
    elif ch=="password":
        print(rd[ch])
    elif ch=="all":
        print(rd)
    else:
        print("Invalid operation")
    f.close()

#info_out("password")

u=''
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

info_update()
