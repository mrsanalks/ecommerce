import pymysql
mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="product"
)
mycursor=mydb.cursor()
num=int(input("enter number of datas"))
for i in range(num):
    product_name=input("enter product name")
    price=int(input("enter price"))
    customer_name=input("enter customer name")
    customer_phone=int(input("enter customer number"))
    sql="insert into product_details(product_name,price,customer_name,customer_phone)values('%s','%d','%s','%d')" %(product_name,price,customer_name,customer_phone)
    mycursor.execute(sql)
    mydb.commit()
print("success")
