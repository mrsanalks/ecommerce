# class A:
#     def fun1(self):
#         print("a")
#
# class B(A):
#     def fun2(self):
#         print("b")
# class C(A):
#     def fun3(self):
#         print("c")
# class D(A):
#     def fun4(self):
#         print("d")
obj=B()
obj.fun1()
obj.fun2()
obj1=C()
obj1.fun1()
obj1.fun3()
obj2=D()
obj2.fun1()
obj2.fun4()
#
# #
# #
# # class details:
# #     def setval(self,id,name,gender):
# #         self.id=id
# #         self.name=name
# #         self.gender=gender
# #         print("id:", self.id)
# #         print("name", self.name)
# #         print("gender:", self.gender)
# #
# # class devoloper(details):
# #     def setval1(self,designation,company):
# #         self.designation=designation
# #         self.company=company
# #         print("designation:", self.designation)
# #         print("company:", self.company)
# #
# # class doctor(details):
# #     def setval2(self,hospital,specialization):
# #         self.hospital=hospital
# #         self.specialization=specialization
# #         print("hospital:",self.hospital)
# #         print("specialization:",self.specialization)
# #
# #
# # obj=devoloper()
# # obj.setval(121,"ayshu","female")
# # obj.setval1("python","tata")
#
#
#
# # by using constructure
#
#
# class details:
#     def __init__(self,id,name,gender):
#         self.id=id
#         self.name=name
#         self.gender=gender
#         print("id:", self.id)
#         print("name", self.name)
#         print("gender:", self.gender)
#
# class devoloper(details):
#     def __init__(self,designation,company,id,name,gender):
#         details.__init__(self,id,name,gender)
#         self.designation=designation
#         self.company=company
#         print("designation:", self.designation)
#         print("company:", self.company)
#
# class doctor(details):
#     def __init__(self,hospital,specialization,id,name,gender):
#         details. __init__(self, id, name, gender)
#         self.hospital=hospital
#         self.specialization=specialization
#         print("hospital:",self.hospital)
#         print("specialization:",self.specialization)
#
# obj=devoloper("python","itc",123,"san","male")
# print()
# obj1=doctor("GMC","ongology","123","ayshu","female")
#

