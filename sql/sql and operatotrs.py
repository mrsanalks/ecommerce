
### and operaotr####


# import pymysql
#
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# c=mydb.cursor()
# id=int(input("enter id"))
# name=input("enter the name")
# sql="select * from table_name where id=%d and name='%s'"%(id,name)
# c.execute(sql)
# a=c.fetchone()
# id=a[0]
# name=a[1]
# email=a[2]
# print("id:",id,"name:",name,"email:",email)

#
# ### and operaotr####
# import pymysql
#
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# c=mydb.cursor()
# sql="select id,name from table_name"
# c.execute(sql)
# a=c.fetchall()
# for i in (a):
#     print(i)






# #### select using or operator#####
#
#
# sql="select * from table_name where condition or condition2"
#
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# product_id=int(input('enter id'))
# product_name=input('enter name')
# sql='select * from product_details where product_id=%d or product_name="%s"'%(product_id,product_name)  # priority is given on first on bcz fetch one
# mycursor.execute(sql)
# a=mycursor.fetchone()
# for i in a:
#       product_id=a[0]
#       product_name=a[1]
#       price=a[2]
#       customer_name=a[3]
#       customer_phone=a[4]
#       print('name=',product_name,'phone number=',customer_phone)
#



#
# sql="select * from table_name where condition or condition2"
#
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# product_id=int(input('enter id'))
# product_name=input('enter name')
# sql='select * from product_details where product_id=%d or product_name="%s"'%(product_id,product_name)  # priority is given on first on bcz fetch one
# mycursor.execute(sql)
# a=mycursor.fetchone()
# product_id=a[0]
# product_name=a[1]
# price=a[2]
# customer_name=a[3]
# customer_phone=a[4]
# print('name=',product_name,'phone number=',customer_phone)


#
# # Q1. using product id
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# product_id=int(input('enter id'))
# sql='select * from product_details where not product_id=%d'%product_id
# mycursor.execute(sql)
# a=mycursor.fetchall()
#
# for i in a:
#     product_id=i[0]
#     product_name=i[1]
#     price=i[2]
#     cutomer_name=i[3]
#     customer_phone=i[4]
#     print('id=',id,'product name=',product_name,'price=',price,'customer name=',cutomer_name,'phone number=',customer_phone)







import pymysql
mydb=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='product'
)
mycursor=mydb.cursor()
product_name=input('enter name')
sql='select * from product_details where not product_name="%s"'%product_name
mycursor.execute(sql)
a=mycursor.fetchall()

for i in a:
    product_id=i[0]
    product_namename=i[1]
    price=i[2]
    cutomer_name=i[3]
    cusomer_phone=i[4]
    print('id=',id,'product name=',product_name,'price=',price,'customer name=',cutomer_name,'phone number=',cusomer_phone)