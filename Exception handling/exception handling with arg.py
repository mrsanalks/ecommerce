# exception handling with arguments
# an exception can have an argument which is a value that gives additional information about the problem.
# the content of the argument changes by the type of exception

# syntax

# try:
#     //code to be excecuted
# except Exceptiontype as Argument:
#     //exception body




# try:
#     //code to be executed
# except exceptiontype as Argument:
#     //exception body
#
# try:
#     a=int(input("enter a"))
#     b=int(input("enter b"))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e :
#     print(e)
# except ValueError as f :
#     print(f)
#
# name=["ayshu","san","farzu"]
# try:
#     position=int(input("enter the position"))
#     print(name[position])
# except IndexError as z :
#     print(z)
#
# import os
# try:
#     filename=input("enter file name")
#     os.remove(fr"C:\Users\SANAL K S\PycharmProjects\python_class\{filename}")
#     print("file removed")
# except FileNotFoundError as e :
#         print(e)

