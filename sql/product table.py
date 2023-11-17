import pymysql
mydb1=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="product"
)

mycursor=mydb1.cursor()
sql="create a table product_details(product_id int auto_increment,product_name varchar(50),price int,customer_name(50),customer_phone bigint(10),primary key(product_id)"


mycursor.execute(sql)
mydb1.commit()
print("success")





# create a table
# product_id
# product_name
# price
# customer_name
# customer_phone
