class A:
    def function1(self):
        print("classA")
# class B:
#     def function2(self):
#         print("classB")
# class C:
#     def function2(self):
#         print("classC")
# class D(A,B,C):
#     def function3(self):
#         print("classD")
#
# obj=D()
# obj.function1()
# obj.function2()
# obj.function3()






# create two son object

#
# class father:
#     def setval(self,name,address):
#         self.nm=name
#         self.adrs=address
#         print("father name:",self.nm)
#         print("address:",self.adrs)
# class mother:
#     def setvalue2(self,name):
#         self.nme=name
#         print("mother name:",self.nme)
# class son(father,mother):
#     def setval3(self,name):
#         self.name=name
#         print("son name:",self.name)
# obj=son()
# obj.setval("CHANDRAN","TVM POOVAR")
# obj.setvalue2("latha")
# obj.setval3("ayshu")
# print()
#
#
# obj1=son()
# obj.setval("CHANDRAN","TVM POOVAR")
# obj.setvalue2("latha")
# obj.setval3("kuttan")
#

#
# #
# class father:
#     def __init__(self,fname):
#         self.nm=fname
# class mother:
#     def __init__(self,mname):
#         self.mm=mname
# class son(father,mother):
#     def __init__(self,fname,mname,sname):
#         father.__init__(self,fname)
#         mother.__init__(self,mname)
#         self.sm=sname
#         print("father name:",self.nm)
#         print("mother name:",self.mm)
#         print("son name:",self.sm)
#
# obj=son("sanal","ayshu","sayush")
# obj1=son("sanal","farzu","sanzu")
#
#
#
#
# class company:
#     def __init__(self,cname,location):
#         self.cnm=cname
#         self.lc=location
#
#
# class teamleader:
#     def __init__(self,teamleader_name,department):
#         self.tm=teamleader_name
#         self.dp=department
#
# class worker(company,teamleader):
#     def __init__ (self,cname,location,teamleader_name,department,emp_name,designation,salary):
#         company.__init__(self, cname, location)
#         teamleader.__init__(self, teamleader_name, department)
#
#         self.em=emp_name
#         self.ds=designation
#         self.salary=salary
#         print("comapny name:",self.cnm)
#         print("loaction",self.lc)
#         print("teamleader:",self.tm)
#         print("deopartment:",self.dp)
#         print("emplyee name:",self.em)
#         print("designmation:",self.ds)
#         print("salary:",self.salary)
# obj=worker("abc","kochi","shigin","it","karthik","devolper",35000)





