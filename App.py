import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", passwd="Admin", database="testdb")
print(mydb)
mycursor=mydb.cursor()
#1 mycursor.execute("CREATE DATABASE testdb")
#2 mycursor.execute("show databases")
#3 for db in mycursor:
#3    print(db)
# as test
mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")
mycursor.execute("show tables")
for tb in mycursor:
    print(tb)