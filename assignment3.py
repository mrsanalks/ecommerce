# Functions without argument
# Write a python program using function to find the cube of a number

# def qube():
#     n=int(input("enter a number"))
#     print("cube = ",n**3)
# qube()


# Using the Lambda function, find the area of a triangle. Take base and height as user input

# x=lambda b,h:1/2*b*h
# b=int(input("enter base of triangle"))
# h=int(input("enter height of triangle"))
# print(x(b,h))


# .Write a Python function that takes list as argument and return second largest
# number of that list
# def find_largest(li):
#     li.sort()
#     return li[-2]
# li=[12,13,85,65,4]
# print("second largest number is ",find_largest(li))


# Create a function that accepts a string as an argument and print a new dictionary
# containing the count of each character in the string
# for example:
# Enter a string: ammu
# Character counts: {'a': 1, 'm': 2, 'u': 1}

# def dic(word):
#     dict={}
#     for i in word:
#         if i in dict :
#             dict[i]+=1
#         else:
#             dict[i]=1
#     print(dict)
# word=input("enter a word")
# dic(word)

# print Fibonacci series using keyword argument
# def fib(num):
#     a = 0
#     b = 1
#     for i in range(num):
#         print(a)
#         c = a + b
#         a = b
#         b = c
# num=int(input("enter a number"))
# fib(num)

# .Calculate the tax amount based on salary find highest tax payers using arbitrary arguments
# Salary>20000 to <50000 tax-2%
# salary>50000to <100000 tax-5%
# Above 100000tax 10%

# def largest_tax(*s):
#     lartax=0
#     for i in s:
#         if i>100000:
#             tax=i*(10/100)
#             print('tax for salary %d=%d'%(i,tax))
#         elif i>50000 and i<=100000:
#             tax=i*(5/100)
#             print('tax for salary %d=%d' % (i, tax))
#         elif i>20000 and i<=50000:
#             tax=i*(2/100)
#             print('tax for salary %d=%d' % (i, tax))
#
#         if lartax<tax:
#             lartax=tax
#         print()
#     print('Highest Tax=',lartax)
#
# largest_tax(120000,80000,30000)
