# overloading is a method or operator that can do diffrent functionlities with the same name and diffrent parameters
# class A:
#     def product(self,a,b):
#         print(a*b)
#
#
#     def product(self,a,b,c):
#         print(a*b*c)
#
# obj=A()
# obj.product(1,2)
# obj.product(1,2,3)


# in the above code we have defined two product method,but we can only use the second product method,as python does not support overloading



          # method to achive method overloading


          # 1    multiple dispach method : it is used for achive method overloading
#
#
#           # pip:python installer package
#           # pip install packagename
# # dispatch is a decorater
from multipledispatch import dispatch
# class A:
#
#     @dispatch(int,int)
#     def product(self,a,b):
#         print(a*b)
#
#
#     @dispatch(int,int,int)
#     def product(self,a,b,c):
#         print(a*b*c)
#
# # obj=A()
# # obj.product(1,2)
# # obj.product(1,2,3)
#
# class A:
#     @dispatch(str,str)
#     def function(self,a,b):
#         print(a+b)
#     @dispatch(float,float)
#     def function(self,a,b):
#         print(a+b)
#     @dispatch(str,int,float)
#     def function(self,a,b,c):
#         print(a,b,c)
# obj=A()
# obj.function("ayshu","sanal")
# obj.function(1.5,1.5)
# obj.function("a",1,1.5)