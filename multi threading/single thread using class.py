# from threading import *
# import time
# class hello(Thread):
#      def __init__(self,a,b):
#          print(a+b)
#          for i in range(5):
#              time.sleep(1.5)
#              print("hello",current_thread().name)
#
# class hai(Thread):
#     def (self,a,b):
#         print(a+b)
#         for i in range(5):
#             time.sleep((1.5))
#             print("hiiii",current_thread().name)
#
# t1=hello()
# t2=hai()
# t1.a(1,2)
# t2.b(5,2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("welcome")



from threading import *
import time
class hello(Thread):
     def __init__(self,a,b):

         Thread.__init__(self)
         self.a=a
         self.b=b
     def run(self):
         print(self.a+self.b,current_thread().name)

class multiply(Thread):
    def __init__(self,a,b,c):
        Thread.__init__(self)
        self.a=a
        self.b=b
        self.c=c
    def run(self):
         for i in range(3):
          print(self.a*self.b*self.c,current_thread().name)


t1=hello(1,2)
t2=multiply(2,3,4)
t1.start()
t2.start()
t1.join()
t2.join()
# t2=b()
# t1.a(1,2)
# t2.b(5,2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
print("welcome")


# run method is entry point for a thread