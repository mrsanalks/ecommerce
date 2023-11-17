
# pip install pymsql
# settings--->packages--->pymsql
import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password=""
)

# create a cursor object
mycursor=mydb.cursor()

# cursor object which is used to select ,retreive data from a set of rows and also it is used to excute an sql command
sql="create database product"
mycursor.execute(sql)
print("database created successfully")
