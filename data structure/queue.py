# queue=[]
# size=int(input("enter the size of queue"))
# top=0
# def enqueue():
#     global top
#     if top==size:
#         print("queue is full")
#     else:
#         el=int(input("enter the element"))
#         queue.append(el)
#         top+=1
#         print(queue)
#
# def dequeue():
#     global top
#     if top==0:
#         print("stack is emptey")
#     else:
#         queue.pop(0)
#         top-=1
#         print(queue)
#
# while True:
#     print("eperation to perform")
#     choice=int(input("1.enqueue\t\tdequeue:"))
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     else:
#         print("invalid input")