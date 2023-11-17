# def hello():
#     return "hi"
# print(hello())
# q write a program to multiply 2 numbers using function with argument and return?

#
# def multiply(a,b):
#     m=a*b
#     return m
# print(multiply(10,20))
# print(multiply(1,2))


# find a number odd or even using function with arg and return

#
# def oddoreven(a):
#     if a%2==0:
#         return"%d is even"%a
#     else:
#         return"%d is odd"%a
# print(oddoreven(5))


#
# def add(num1,num2):
#     return num1+num2
#
# def sub (num,num2):
#     return num1-num2
#
# def mul(num,num2):
#     return num*num2
#
# def div(num,num2):
#     return num/num2
#
# print("SIMPLE CALCULATOR")
#
# print("option")
#
# print(" 1 for add\n 2 for sub\n 3 for mul\n 4 for div")
#
# choice=input("enter choice(1/2/3/4):")
# if choice in[1,2,3,4]:
#     num1 = float(input("enter a number"))
#     num2 = float(input("enter number 2"))
#     if choice == 1:
#        print(num1, "+", num2, "=", add(num1, num2))
#
#      elif choice==2:
#          print(num1, "-", num2, "=", sub(num1, num2))
#
#      elif choice == 3:
#          print(num1, "*", num2, "=", mul(num1, num2))
#
#     elif choice == 4:
#         print(num1, "/", num2, "=", div(num1, num2))
#
# else:
#     print("invalid")
#


# lambda function
#  variable-name= labmbda arguments:expression(a+b)


#
# def add(a,b):
#    return a+b
# print(add(1,2))


#
# x=lambda a,b:a+b
# print(x(12,23))
# # string
# x=lambda s:"my name is %s"%s
# print(x("farzu"))



# solve a/b*c using lamda function?

#
#
# x=lambda a,b,c:a/(b*c)
# a=int(input("enter a"))
# b=int(input("enter b"))
# c=int(input("enter c"))
# print(x(a,b,c))


# find square root of  number
#
# x=lambda a:a**0.5
# a=int(input("enter a"))
# print(x(a))
#
# find cube of an arguemnt?
# x=lambda a:a**3
# a=int(input("enter a"))
# print(x(a))

# # find area of circle
# x=lambda a:3.14*(a**2)
# a=int(input("enter radious of circle"))
# print(x(a))







