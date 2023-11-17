# # # 1.
# lis=[1,2,3]
# new=[]
#
# def factorial(lis):
#
#     val=1
#     for i in lis:
#           val*=i
#           new.append(val)
#     print(new)
#
# factorial(lis)










# 2.
n=int(input("enter a number"))
for i in range (n):
    for k in range (n-i-1):
        print(" ",end=' ')
    for j in range (i+1):
        print("*",end=" ")
    print()



#3.
# dit={"val1":1,
#      "val2":2,
#      "val3":3,
#      "val4":4,
#      "val5":6,
#    }
# for j,i in dit.items():
#     if i%2==0:
#         print(j,i)
#


# 4'

# lis=['a','a','b','b','c']
# b=set(lis)
# print(list(b))



# 5
# list=[1,2,3,4,5]
# def min(*a):
#     list.sort()
#     min=list[0]
#     return(min)
# def max(*a):
#     list.sort()
#     max=list[-1]
#     return (max)
# print(min(list))
# print(max(list))