# import pymysql
#
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# num=int(input("enter the no: of datas"))
# for i in range (num):
#     name = input("enter name")
#     email = input("enter mail")
#     phone_number = int(input("number"))
#     sql = "insert into table_name(name,email,phone_number)values('%s','%s','%d')" % (name, email, phone_number)
#     mycursor.execute(sql)
#     mydb.commit()


print("data added successfully")