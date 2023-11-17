from threading import *
import time

def cube(a):
    print("calculate cube")
    for i in a:
        time.sleep(1.5)
        print("cube:",i**3,current_thread().name)

def square(a):
    print("count square")
    for i in a:
        time.sleep(1.5)
        print("square:",i**2,current_thread().name)

li=[1,2,3,4]
t1=Thread(target=square,args=(li,))
t1.setName("first_thread")
t2=Thread(target=square,args=(li,))
t2.setName("second_thread")
t1.start()
t2.start()
t1.join()
t2.join()