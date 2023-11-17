# Q1. Write a program that takes a number as input and prints it's prime factors using for loop


# n=int(input("Enter a number:"))
# print("Prime factors are:")
# for i in range(2,n):
#     if n%i==0:
#       print(i)
#       n//=i


# Q2.Python program to count the total number of digits in a number

# n=int(input("enter a number"))
# count = 0
# for i in str(n):
#     num = n// 10
#     count += 1
# print("No of digit in the number is: ", count)


# Q3.Multiplication table

# n=int(input("Multiplication table for n = "))
# for i in range(1,n+1):
#      for j in range(1,n+1):
#          print(i*j,end="\t")
#      print()

# Q4. Print following pattern
# 1
# 2	2
# 3	3
# 4	4	4
#
# row = int(input('Enter number of rows required: '))
# for i in range(row):
#   for j in range(row - i):
#     print(' ', end='')
#   for j in range(2 * i + 1):
#     if j == 0 or j == 2 * i or i == row - 1:
#         print(i+1, end='')
#     else:
#        print(' ', end='')
#   print()


# Q5&6 PATTERN

    # * * *
	# * * *
	# * * *
	#   *
	# * * *
	# * * *
	# * * *

#
# n=3
# for i in range(n):
#   for j in range(n):
#     print("*",end=" ")
#   print("")
# for k in range(1):
#   for m in range(1):
#     print(" ","*",end=" ")
#   print("")
# for i in range(n):
#   for j in range(n):
#     print("*",end=" ")
#   print("")




	#    *
    #    * *
    #   * * *
    #  * * * *
    #  * * * *
    #   * * *
    #    * *
    #     *

# n=int(input("enter the number"))
# for i in range(n):
#   for k in range(n-i):
#      print("",end=" ")
#   for j in range(i+1):
#      print("*",end=" ")
#   print("")
# for i in range(n):
#   for k in range(0,i+1):
#     print("",end=" ")
#   for j in range(n-i):
#     print("*",end=" ")
#   print("")








































