# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# sql="select * from table_name order by name"
# mycursor.execute(sql)
# a=mycursor.fetchall()
#
# for i in (a):
#     id=i[0]
#     name=i[1]
#     mail=i[2]
#     phone=i[3]
#     print("id:",id,"name:",name,"email:",mail,"phone:",phone)


# select product name and price from product table ,order product by price:
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
# mycursor=mydb.cursor()
# sql="select product_name,price from product_details order by price"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     product_name=i[0]
#     price=i[1]
#     print("product name:",product_name,"price:",price)



# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="product"
# )
# mycursor=mydb.cursor()
# sql="select product_name,price from product_details order by price desc"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     product_name=i[0]
#     price=i[1]
#     print("product name:",product_name,"price:",price)






import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="product"
)
mycursor=mydb.cursor()
sql="select product_name,price from product_details order by price asc,product_name desc"
mycursor.execute(sql)
a=mycursor.fetchall()
for i in a:
    product_name=i[0]
    price=i[1]
    print("product name:",product_name,"price:",price)






