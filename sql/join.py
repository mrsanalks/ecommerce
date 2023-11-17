# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="product"
# )
# mycursor=mydb.cursor()
# sql='create table product_new(id int auto_increment,product_name varchar(50),features varchar(50),primary key(id))'
#
# mycursor.execute(sql)
# mydb.commit()
# print("success")

#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="product"
# )
# # mycursor=mydb.cursor()
# num=int(input("enter number of datas"))
# for i in range(num):
#     product_name=input("enter product name")
#     features=input("enter features")
#     sql="insert into product_new(product_name,features)values('%s','%s')" %(product_name,features)
#     mycursor.execute(sql)
#     mydb.commit()
# print("success")




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
# sql="select product_details.product_name,product_details.customer_name,product_new.features,product_new.product_name from product_details inner join product_new on product_details.product_id=product_new.id"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     product_name=i[0]
#     customer_name=i[1]
#     features=i[2]
#     print("product name:",product_name,"customer_name:",customer_name,"features:",features)
#
#






#
#
#


# create a table students with fields id,student_name,roll ,school_name
# create another table marklist id,maths chemistrty ,english
# 3 datas insert
# inner join student and marklist using roll_no
# student_name,maths,chem,english

#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# sql="create table students(id int auto_increment,student_name varchar(50),roll_no int,school_name varchar(50),primary key(id))"
#
# mycursor.execute(sql)
# mydb.commit()
# print("success")
#

#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# num=int(input("enter number of datas"))
# for i in range(num):
#     student_name=input("enter student name")
#     school_name=input("enter school name")
#     roll_no=int(input("enter roll number"))
#     sql="insert into students(student_name,roll_no,school_name)values('%s','%d','%s')" %(student_name,roll_no,school_name)
#     mycursor.execute(sql)
#     mydb.commit()
# print("success")
#


#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# sql="create table markslist(id int auto_increment,roll int,maths varchar(50),chemistry varchar(50),english varchar(50),primary key(id))"
#
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
# num=int(input("enter number of datas"))
# for i in range(num):
#     roll = int(input("enter roll number"))
#     maths=int(input("enter maths mark"))
#     chemistry=int(input("enter chemistry mark"))
#
#     english=int(input("enter english mark"))
#     sql="insert into markslist(roll,maths,chemistry,english)values('%d','%d','%d','%d')" %(roll,maths,chemistry,english)
#     mycursor.execute(sql)
#     mydb.commit()
# print("success")

#
#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# sql="select students.student_name,markslist.maths,markslist.chemistry,markslist.english from students inner join markslist on students.roll_no=markslist.roll"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# print("maths","\t\tchemistry","\t\tenglish","\t\t\tname")
# for i in a:
#     student_name=i[0]
#     maths=i[1]
#     chemistry=i[2]
#     english=i[3]
#     print(" ",maths,'\t\t ',chemistry,'\t\t\t ',english,'\t\t\t  ',student_name)

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
#
#
# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# sql="alter table markslist add total int as (maths+chemistry+english)"
# mycursor.execute(sql)
# mydb.commit()
# print("success")
#


# query to drop a column

# sql="alter table student drop column name"




# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ayshdata"
# )
# mycursor=mydb.cursor()
# sql="alter table table_name drop location"
# mycursor.execute(sql)
# mydb.commit()
# print("success")



###### to drop a table#####



# sql="drop table table_name"




###########truncate#########


# it remove all the raws from a table but the table structure remains
# sql="truncate table table_name"

##########delete database##########
# sql="drop database database_name"


























