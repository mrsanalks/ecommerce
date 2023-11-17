# syntax
# try:
#    code to be executed

# except:
#      catch the exception



# # zero divison error
# a=int(input("enter a"))
# b=int(input("enter b"))
# c=a/b
# print(c)

# try:
#     a = int(input("enter a"))
#     b = int(input("enter b"))
#     c = a / b
#     print(c)
# except:
#     print("cannot divide by zero..")

# # solve quadratic equation using exception handling
#
# try:
#     a=int(input("enter a"))
#     b=int(input("enter b"))
#     c=int(input("enter c"))
#     d=(b**2-4*a*c)**0.5
#     x1=(-b+d)/(2*a)
#     x2=(+b+d)/(2*a)
#     print(x1)
#     print(x2)
# except:
#     print("value of a cant be zero")


# value error

# try:
#     a=int(input("enter a"))
#     print(a)
# except:
#     print("plz input an integrer")


# zerodivison error


# try:
#     a = int(input("enter a"))
#     b = int(input("enter b"))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("value error")

# indexerror:it occurs when an invalid index is given

# name=["ayshu","san","farzu"]
#
# try:
#     position=int(input("enter the position"))
#     print(name[position])
# except IndexError:
#     print("list index out of range")
# except ValueError:
#     print("value error")


#
# # file not found error
# import os
#
# try:
#     filename=input("enter the file name")
#     os.remove(fr"C:\Users\SANAL K S\PycharmProjects\python_class\{filename}")
#     print("removed")
# except FileNotFoundError:
#     print("file not found")
#
# except ValueError:
#     print("value error")

#
# a=int(input("enter a name"))
# print(b)