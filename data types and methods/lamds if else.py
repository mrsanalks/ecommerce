# find square of a number if number gtreater than 0 ?


# (none=null vale)

# x=lambda a:a**2 if a>0 else None
# print(x(5))

# find a number negative or positive using lamda?
# x=lambda a:"psitive"  if a>0 else "negative"
# a=int(input("enter a"))
# print(x(a))

# find the largest of two numbers using lambda?
# x=lambda a,b:"%d is greater"%a if a>b else "%d is greater"%b
# a=int(input("enter a"))
# b=int(input("enter b"))
# print(x(a,b))



# # convert a positive number into negative number and a negative number to postive number using lanbda?
# x=lambda a:a*-1  if a>0 else -1*a
# a=int(input("enter a number"))
# print(x(a))
#
# x=lambda a:-a  if a>0 else -a
# a=int(input("enter a number"))
# print(x(a))


# # find a number is odd or even?
# x=lambda a:"even"  if a%2==0 else "odd"
# a=int(input("enter a number"))
# print(x(a))



# write a program to find the largest of three numbers using lambda?

# x=lambda a,b,c:"%d is greater"%a if a>b and a>c else("%d is greater"%b if b>c else "%d is greater"%c)
# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# print(x(a,b,c))
# find smallest number of three numbers input by the user


#
# x=lambda a,b,c:"%d is smaller"%a if a<b and a<c else("%d is smaller"%b if b<c else "%d is smaller"%c)
# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# print(x(a,b,c))

# find a number is positive or negative or zero
# x=lambda a:"postive" if a>0 else("negative" if a<0 else "zero")
# a=int(input("enter a number"))
# print(x(a))

# find largest of 4 numbers
# x=lambda a,b,c,d:"%d is greater"%a if a>b and a>c and a>d else("%d is greater "%b if b>c and b>d else("%d is greater"%c if c>d else "%d is greater"%d))
# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# d=int(input("enter number"))
# print(x(a,b,c,d))

# accept age of 4 people and display the youngest one
# youngest=lambda a,b,c,d:'%d is youngest'%a if a<b and a<c and a<d else('%d is youngest'%b if b<c and b<d else('%d is youngest'%c if c<d else '%d is youngest'%d))
# a=int(input('enter the age of first person'))
# b=int(input('enter the age of second person'))
# c=int(input('enter the age of third person'))
# d=int(input('enter the age of the fourth person'))
# print(youngest(a,b,c,d))



# variable_name=list(filter(lambda arguments:expression,list_variable))



# write a lambda function to filter out even number from given list
# lis=[1,2,3,4,5,6,7,8,9]
# x=list(filter(lambda i:i%2==0,lis))
# # print(x)
# odd=list(filter(lambda i:i%2!=0,lis))
# print(odd)


# from given list filter out numbers which is divicible by 13 not by 3
#
# li=[1,213,100,220,1011,33,13]
# a=list(filter(lambda i:i%13==0 and i%3!=0,li))
# print(a)

# from the given list filtr out ages between 18 and 50
#
# age=[12,34,28,2,50,22,1]
# a=list(filter(lambda i:i>18 and i<50,age))
# print(a)


# map
# variable_name=list(map(lambda arguments:expression,list_variable))
#
# l=[2,3,4,5,6]
# x=list(map(lambda i:i**2,l))
# print(x)


# find square root of each elements in given list
#
# l=[1,4,9,16,25,36]
# x=list(map(lambda i:i**0.5,l))
# print(x)

# create a list from  1 to 10
# # enter number=6
# lis=[1,2,3,4,5,6,7,8,9,10]
# a=int(input("enter a number"))
# x=list(map(lambda i:i*a,lis))
#
# print(x)


#  zipfunctinon (pair akkan use cheyyum)
# name=("san","ayshu","farzu")
# age=(12,25,23)
# a=zip(name,age)
# print(list(a))


# map function using two list(
# lis=[1,2,3,4]
# lis2=[4,5,6,7]
# a=list(map(lambda x,y:x+y ,lis,lis2))
# print(a)


# convert the first letter to uppercase
# lis=["alan","alan alan","amal amal"]
# a=list(map(lambda i:i.capitalize(),lis))
# print(a)
from functools import reduce

# find the largest elements from the list using reduce
# li=[100,400,300]
# max=reduce(lambda a,b:a if a>b else b,li)
# print(max)

# find smallest element from given list

# lis=[2,1,3,5,7]
# min=reduce(lambda a,b:a if a<b else b,lis)
# print(min)

# find the product of numbers from given list
# lis=[5,7,9,11,13]
# product=reduce(lambda a,b:a*b ,lis)
# print(product)

# find sum of elements in the list
# lis=[1,2,3,4,5,6]
# sum=reduce(lambda a,b:a+b,lis)
# print(sum)



