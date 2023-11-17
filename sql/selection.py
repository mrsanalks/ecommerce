# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# sql="select * from table_name"
# # *  is a universal symbol that is used to select all datas
# mycursor.execute(sql)
# a=mycursor.fetchall()
# # fetchall :it is used to fetch all datas and return a list of tuple
# # print(a)
#
# for i in (a):
#     id=i[0]
#     name=i[1]
#     mail=i[2]
#     phone=i[3]
#     print("id:",id,"name:",name,"email:",mail,"phone:",phone)

########### to return one data

#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# id=int(input("enter id"))
# sql="select * from table_name where id=%d"%id
# mycursor.execute(sql)
# # fetchone:it is used to fetch a single row of data,it returns a singlr tuple
# a=mycursor.fetchone()
# id=a[0]
# name=a[1]
# phone=a[2]
# email=a[3]
# print("id:",id,"name:",name,"phone:",phone,"email:",email)



import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ayshdata"
)
mycursor=mydb.cursor()
name=input("enter name")
sql="select * from table_name where name='%s'"%name
mycursor.execute(sql)
# fetchone:it is used to fetch a single row of data,it returns a singlr tuple
a=mycursor.fetchone()
phone=a[2]
email=a[3]
print("phone:",phone,"email:",email)