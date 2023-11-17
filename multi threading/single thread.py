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
        time.sleep(10)
        print("square:",i**2,current_thread().name)

li=[1,2,3,4]
cube(li)
square(li)

#current thread.name: this function is used to get the name  current working thread of a process



# main thread: it is called a single theread in which a process that execute in a single thread during the running of a programm


