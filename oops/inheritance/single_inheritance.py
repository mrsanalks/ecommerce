# # it is a method with single child class that access the ,method of single parent class
# class A:#PARENT
#     def setvalue(self):
#         print("parent")
# class B(A):
#     def setvalue1(self):
#         print("child")
# #
# # objct=B()
# # objct.setvalue()
# # objct.setvalue1()
#
#
# # company---> parent class
# # employee--.childclass
#
# class company:
#
#     def setval2(self,company_name,location):
#         self.cmp=company_name
#         self.lcn=location
#         print("company name",self.cmp)
#         print("location:",self.lcn)
#
# class employees(company):
#     def setval1(self,emp_name,id,number,salary):
#         self.nm=emp_name
#         self.id=id
#         self.nmbr=number
#         self.slry=salary
#         print("name:",self.nm)
#         print("id:",self.id)
#         print("number:",self.nmbr)
#         print("salary:",self.slry)
# obct=employees()
# obct.setval2('abc',"kannur")
# print()
# obct.setval1("san","25","952",985623)






# # single iheritance using comstructor
#
#
# class A:
#     def __init__(self):
#         print("parent class")
# class B(A):
#     def setval(self):
#         print("child")
#         super().__init__()
# obct=B()
# # obct.setval()
#
# class vehicle:
#     def __init__(self,name,number):
#         self.nme=name
#         self.nmbr=number
#         print("vehicle name:",self.nme)
#         print("number:",self.nmbr)
# class car(vehicle):
#     def __init__(self,name,number,color,price):
#         super().__init__(name,number)
#         self.clr=color
#         self.pr=price
#         print("color:",self.clr)
#         print("price:",self.pr)
#
# objct=car("kia","856","black","25000000")








# implement a single


# class transpotation:
#     transpotatio_type="kannur"
#     def __init__(self,ksrtc,privetbus):
#         self.kstrc=ksrtc
#         self.pvtbus=privetbus
#         print("")




















