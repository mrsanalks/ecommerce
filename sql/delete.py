# # # import pymysql
# # # mydb=pymysql.connect(
# # #     host="localhost",
# # #     user="root",
# # #     password="",
# # #     database="ayshdata"
# # # )
# # #
# # # mycursor=mydb.cursor()
# # # id=int(input("enter id to dlt"))
# # # sql="delete from table_name where id=%d"%id
# # # mycursor.execute(sql)
# # # mydb.commit()
# # # print("row dltd")
# #
# #
# # # dlt using product name and customername
# #
# #
# #
# #
# # import pymysql
# # mydb=pymysql.connect(
# #     host="localhost",
# #     user="root",
# #     password="",
# #     database="product"
# # )
# #
# # mycursor=mydb.cursor()
# # name=input("enter product name")
# # customer=input("enter customer name to dlt")
# # sql1="select product_name,customer_name from product_details"
# # mycursor.execute(sql1)
# # a=mycursor.fetchall()
# # for i in a:
# #     if name==i[1] and customer==i[3]:
# #         sql="delete from product_details where product_name='%s',customer_name='%s'"%(name,customer)
# #         mycursor.execute(sql)
# #         mydb.commit()
# #         print("success")
# #         break
# # else:
# #     print("data not found")
# #
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# limit=int(input("enter the limit"))
# sql="select * from table_name  limit=%d"%limit
#
# # *  is a universal symbol that is used to select all datas
# mycursor.execute(sql)
# a=mycursor.fetchall()
# # fetchall :it is used to fetch all datas and return a list of tuple
# # print(a)
#
# for i in a:
#     id=i[0]
#     name=i[1]
#     mail=i[2]
#     phone=i[3]
#     print("id:",id,"name:",name,"email:",mail,"phone:",phone)
