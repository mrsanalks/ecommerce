# same method name with same number of arguments
# it is used to change behavior of existing methods,and there is a need for atleast two classes for method overriding
# in overriding inheritance always required as it is done between parent class (super class) and childclass (baseclass)
# # methods
#
# class father:
#     def phone(self):
#         print("fathers phone")
# class child(father):
#     pass
#
# obj=child()
# obj.phone()


# overriding

#
# class father:
#     def phone(self):
#         print("fathers phone")
# class child(father):
#     def phone(self):
#         print("child phone")
#
#
# obj=child()
# obj.phone()
#

# child phone method overrides fathers phone method




#
# # multiple inheritance
#
# class A:
#     def fun(self):
#         print("a")
#
# class B:
#     def fun1(self):
#         print("b")
# class C(A,B):
#     def fun(self):
#         print("c")
#     def fun1(self):
#         print("b")
# obj=C()
# obj.fun()
# obj.fun1()
# class c overrides class a and class b

# over riding using multilevel inheritance
#
# class A:
#     def fun(self):
#         print("a")
#
# class B(A):
#     def fun1(self):
#         print("b")
# class C(B):
#     def fun(self):
#         print("c")
#
#
# obj=C()
# obj.fun()























