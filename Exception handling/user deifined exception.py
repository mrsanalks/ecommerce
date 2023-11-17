# # in python,user can define custom exceptions by creating a new class
# # this exception class has to be derived,either directly or indirectly,
# # from the build-in Exception class,most of the build-in exception are also derived this  class
#
#
# class zeroerror(Exception):
#     pass
# class negativeerror(Exception):
#      pass
#
# try:
#     num=int(input("enter a number"))
#
#     if num==0:
#         raise zeroerror
#     elif num<0:
#         raise negativeerror
#     else:
#         print("success")
# except zeroerror:
#     print("zero error occured")
# except negativeerror:
#     print("negative error occured")

class old(Exception):
    pass
class young(Exception):
    pass
try:
    age=int(input("enter age"))
    if age>=50:
        raise old
    elif age<21:
        raise young
    else:
        print("you are registered")
except old:
    print("you are old chetta")
except young:
    print("you are young vro")