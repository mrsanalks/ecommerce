# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="product"
# )
#
# mycursor=mydb.cursor()
# product_name=input("enter product name")
# limit=int(input("enter limit"))
# sql="select * from product_details where product_name='%s' limit %d"%(product_name,limit)
# mycursor.execute(sql)
# data=mycursor.fetchall()
# for i in data:
#     id=i[0]
#     customer_name=i[3]
#     print("id:",id,"name:",customer_name)

#
#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="product"
# )
#
# mycursor=mydb.cursor()
# sql="select min(price) from product_details"
# mycursor.execute(sql)
# i=mycursor.fetchone()
# print(i[0])
#
#

#
#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="product"
# )
#
# mycursor=mydb.cursor()
# sql="select max(price) from product_details"
# mycursor.execute(sql)
# # i=mycursor.fetchone()
# # print(i[0])
#
#
#
#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="product"
# )
#
# mycursor=mydb.cursor()
# sql="select min(price),max(price) from product_details"
# mycursor.execute(sql)
# i=mycursor.fetchone()
# print(i)




import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="product"
)

mycursor=mydb.cursor()
sql="select avg(price) from product_details"
mycursor.execute(sql)
i=mycursor.fetchone()
print(i[0])






