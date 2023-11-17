# class: class is collection of objects
# class is a blueprint of an object

# laptop:class
# hp,azus:objects
# #
# class class_name:
#     def function_name(self):
#         print("hello")
# obj=class_name()
# obj.function_name()

# member_function= a function that defined inside  a class called member functiom or method


# # add 2 numbers
# class add:
#     def abc(self,a,b):
#         print(a+b)
# obj=add()
# obj.abc(1,2)

# object creation
# object:it is real world entities
# it is an instance of class

class laptop:
    def setval(self,name,os,ram,price):      #self:self variable of member function
        self.name=name
        self.os=os
        self.ram=ram
        self.price=price
        print('laptop name=',self.name)
        print('os=',self.os)
        print('ram=',self.ram)
        print('price=',self.price)
obj=laptop()
obj.setval('hp','windows','8gb',52000)
obj1=laptop()
obj.setval('dell','windows','8gb',30000)


# Q create a class person with arguments
# pers name,age,gender,height,weight
# creat 3 person object

# class pers:
#     def p(self,name,age,gender,height,weight):
#         self.nm=name
#         self.ag=age
#         self.gen=gender
#         self.hei=height
#         self.wei=weight
#         print('name=',self.nm)
#         print('age=',self.ag)
#         print('gender=',self.gen)
#         print('height=',self.hei)
#         print('weight=',self.wei)
# object=pers()
# object.p('shigin',27,'male',171,63)     here repalcing of shigin to drishya in object
# object.p('drishya',25,'female',168,55)   so we are creating seperate reference variable
# object.p('unni',29,'male',172,75)

# or
# object=pers()
# object.p('shigin',27,'male',171,63)    #reference variable name is changed to find seperate products
# object1=pers()
# object1.p('drishya',25,'female',168,55)
# object2=pers()
# object.p('unni',29,'male',172,75)