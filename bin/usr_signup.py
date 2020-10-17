#sign_up screen 1
#asks the user to enter his/her mysql password 
import mysql.connector as sql #pip install mysql-connector-python
usr = input("Enter your MySQL user-name : ")
try:
    pwd = input("Enter your MySQL password: ")
    c = sql.connect(host = "127.0.0.1", user = usr, passwd = pwd)
except:
    print("Uh oh! It looks like i could not connect to MySQL, please make sure MySQL is properly installed and you have entered the correct username and password.")

cur = c.cursor()
cur.execute("create database if not exists user_info_christmas_presents_for_nsa;")
