#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#
#
# )
# mycursor=mydb.cursor()
# sql="create database sample"
# mycursor.execute(sql)
# print("database created")

# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="sample"
# )
#
#
#
# mycursor=mydb.cursor()
# # id name phone email
# sql="create table sample(id int auto_increment,name varchar(50),primary key(id))"
#
# mycursor.execute(sql)
# mydb.commit()
# print("table created succesfully")


#
# import pymysql
#
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="sample"
# )
# mycursor=mydb.cursor()
# num=int(input("enter the no: of datas"))
# datasfor i in range (num):
#     name = input("enter name")
#
#     sql ="insert into sample(name)values('%s')" % (name)
#     mycursor.execute(sql)
#     mydb.commit()



# import pymysql
#
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="sample"
# )
# mycursor=mydb.cursor()
# sql="truncate table sample"
# mycursor.execute(sql)
# mydb.commit()
# print("truncated")
#
# import pymysql
#
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="sample"
# )
# mycursor=mydb.cursor()
# sql="drop table sample"
# mycursor.execute(sql)
# mydb.commit()
# print("drop a table")


import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="sample"
)
mycursor=mydb.cursor()
sql="drop database sample"
mycursor.execute(sql)
mydb.commit()
print("deleted database")

