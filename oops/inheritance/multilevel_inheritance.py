# class A:
#     def fun1(self):
#         print("a")
# class B(A):
#     def fun2(self):
#         print("b")
# class C(B):
#     def fun3(self):
#         print("c")
# obj=C()
# obj.fun1()
# obj.fun2()
# obj.fun3()

# mobile(storage,color)
# samsang(ram)
# samgalaxy(speed)

#
# class mobile:
#     def setval(self,storage,color):
#         self.storage=storage
#         self.color=color
# class samsung(mobile):
#     def setvl1(self,ram):
#         self.ram=ram
#
# class samsung_galaxy(samsung):
# #     def setval2(self,speed):
# #         self.speed=speed
# #         print("storage:",self.storage)
# #         print("color:",self.color)
# #         print("ram:",self.ram)
# #         print("speed:",self.speed)
# # obj=samsung_galaxy()
# # obj.setval("62gb","red")
# # obj.setvl1("6gb")
# # obj.setval2("2.5ghz")
# #
# #
#
# # car:wheel,color
# # maruthi:800
# # maruthi800:price
#
#
#
#
# class car:
#     def __init__(self,wheel,color):
#         self.wheel=wheel
#         self.color=color
# class maruthi(car):
#     def __init__(self,wheel,color,model):
#         car.__init__(self,wheel,color)
#         self.model=model
#
# class maruthi800(maruthi):
#     def __init__(self,wheel,color,model,price):
#         maruthi.__init__(self,wheel,color,model)
#         self.price=price
#         print("wheel:",self.wheel)
#         print("color:",self.color)
#         print("model:",self.model)
#         print("price:",self.price)
# obj=maruthi800("mrf","black",2000,35000)
