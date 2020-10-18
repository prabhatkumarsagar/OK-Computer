#sign_up screen 1
#asks the user to enter his/her mysql password 
import mysql.connector as sql #pip install mysql-connector-python

while True:
    try:
        usr = input("Enter your MySQL username('root' by default): ")
        pwd = input("Enter your MySQL password: ")
        if usr=='':
            usr="root"
        con = sql.connect(host = "127.0.0.1", user = usr, passwd = pwd)
    except:
        print("Uh oh! It looks like i could not connect to MySQL, please make sure MySQL is properly installed and you have entered the correct username and password.")
        break
cur = con.cursor()
cur.execute("create database if not exists pydeskassist;")
cur.execute("use pydeskassist;")
cur.execute("create table if not exists usr_info(S_No int(1), Name varchar(100), DOB date, Gender(M/F) char(1), Email varchar(100), Password varchar(30));

#sign_up screen 2