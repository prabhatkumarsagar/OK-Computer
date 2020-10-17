#sign_up screen 1
#asks the user to enter his/her mysql password 
import mysql.connector as sql #pip install mysql-connector
try:
    pwd=input("Enter you MySQL username: ")
    c=sql.connect(host="127.0.0.1",user="root",passwd=pwd)
except:
    print("Uh oh! It looks like i could not connect to MySQL, please make sure MySQL is properly installed and you have entered the correct password.")

cur=c.cursor()
cur.execute("create database user_info;")
