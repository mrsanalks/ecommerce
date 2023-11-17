# class employee:
#     def __init__(self,name,salary):
#         #public data members
#         self.name=name
#         self.__salary=salary
#     def fun(self): #public function
#         print('name = ',self.name,'salary = ',self.__salary)
# obj=employee("ayshu",500)
# obj.fun()
# print("name:",obj.name)
# print("salary:",obj__salary)

# # 1.nam mangling
#
# # _classname__datamember
# class employee:
#     def __init__(self,name,salary):
#         #public data members
#         self.name=name
#         self.__salary=salary
#     def __fun(self): #public function
#         print('name = ',self.name,'salary = ',self.__salary)
# obj=employee("ayshu",500)
# obj._employee__fun()
# print("name:",obj.name)
# obj._employee__fun()
# print("salary:",obj._employee__salary)
