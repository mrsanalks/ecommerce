# abstraction in python is difined as a process of handling complexity by hiding unnecessory information from user
# this is one of the core concepts of object-priented programming (OOP)language
# what is ABC in abstract?
# this module provides the infrastructure for defining abstract base classes

# abc:python has a module called abc(abstract base class)that offers the necessory tools for crafting an abstract base class

# @abstractmethod : a decorator indicating abstract methods
# what is decorator?
# decorators can be extreamely usefull as the allow the extension of an existing function,without any modification to the-
# original function source code

from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def wheel(self):
#         pass
#
#     @abstractmethod
#     def door(self):
#         pass
#
# class car(vehicle):
#     def wheel(self):
#         print("4 wheels...")
#     def airbag(self):
#         print("have airbag")
#     def door(self):
#         print("4 doors")
# # obj=car()
# # obj.wheel()
# # obj.airbag()
# # obj.door()
# from abc import ABC,abstractmethod
#
# class animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#     @abstractmethod
#     def eyes(self):
#         pass
# class dog(animal):
#     def sound(self):
#         print("woof")
#
#     def eyes(self):
#         print("two eyes")
#     def tail(self):
#         print("have tail")
# class cow(animal):
#     def sound(self):
#         print("moo")
#
#     def eyes(self):
#         print("two eyes")
#     def milk(self):
#         print("cow has milk")
#
# obj=dog()
# obj.eyes()
# obj.sound()
# obj.tail()
# print()
# obj1=cow()
# # obj1.sound()
# # obj1.eyes()
# # obj1.milk()
# from abc import ABC,abstractmethod
# class A(ABC):
#    @abstractmethod
#    def __init__(self,name,adress):
#        pass
#
# class B(A):
#     def __init__(self,name,adress):
#         super().__init__(name,adress)
#         self.name=name
#         self.adress=adress
#         print("name:",self.name,"\t\tadress:",self.adress)
#         def hello(self):
#             print("hello")
# obj=B("AYSHU","XYZ")



