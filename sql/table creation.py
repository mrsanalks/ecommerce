# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
#
#
#
# mycursor=mydb.cursor()
# # id name phone email
# sql="create table table_name(id int auto_increment,name varchar(50),email varchar(50),phone_number bigint(10),primary key(id))"
#
# mycursor.execute(sql)
# mydb.commit()
# print("table created succesfully")
# # commit refers to the saving  of data permenantly after a set changes


#
# # create a table
# # product_id
# # product_name
# # price
# # customer_name
# # customer_phone
#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="product_details"
# )
#
# mycursor=mydb.cursor()
# sql="create table product_details(product_id int auto_increment,product_name varchar(50),price int,customer_name varchar(50),customer_phone bigint(10),primary key(product_id))"
# mycursor.execute(sql)
# mydb.commit()
# print("success")
#

