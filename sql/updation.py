# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# id=int(input("enter id"))
# name=input("enter new name")
# sql="update table_name set name='%s' where id='%d'"%(name,id)
# mycursor.execute(sql)
# mydb.commit()
# print("success")
















####multiple datas updation####
# sql="update table_name set email=%'s',phone=%'d' where id=%'d'"



# # update customer name and phone number
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
# product_id=int(input("enter id"))
# customer_name=input("enter new customer name")
# customer_phone=int(input("enter number"))
# sql="update product_details set customer_name='%s',customer_phone=%d where product_id=%d"%(customer_name,customer_phone,product_id)
# mycursor.execute(sql)
# mydb.commit()
# print("success")


# update table set phone=%d where email=%'s' and name='%s'

# qstn pro_price using id and pro name

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
# product_id=int(input("enter id"))
# customer_name=input("enter  customer name")
# customer_phone=int(input("enter new number"))
# product_name=input("enter product")
# sql="update product_details set customer_phone=%d where customer_name='%s' and product_name='%s'"%(customer_phone,customer_name,product_name)
# mycursor.execute(sql)
# mydb.commit()
# print("success")



#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# sql="alter table table_name add location varchar(200)"
# mycursor.execute(sql)
# mydb.commit()
# print("success")


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
# location=input("enter location")
# sql="update table_name set location='%s' where id=%d"%(location,id)
# mycursor.execute(sql)
# mydb.commit()
# print("success")