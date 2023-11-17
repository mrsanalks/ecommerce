# Write a Python program to calculate the area of a circle
#
# radious=float(input("enter a radious"))
# area=3.14159*(radious**2)
# print("area :",area)

#
# radius = float(input("Enter the radius of the circle: "))
# area = 3.14159 * (radius ** 2)
#
# print(f"The area of the circle with radius {radius} is {area:.2f}")

# num = int(input("Enter a number: "))
#
# if num < 0:
#     print(f"{num} is not a perfect square because it's negative.")
# else:
#     sqrt = int(num ** 0.5)
#     if sqrt * sqrt == num:
#         print(f"{num} is a perfect square.")
#     else:
#         print(f"{num} is not a perfect square.")



# # change this value for a different result
# celsius = 65.5556
#
# # calculate fahrenheit
# fahrenheit = (celsius * 1.8) + 32
# print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))



# print("hello world"+" hello")
#
# ''' -----------------------MACHINE TEST---------------------------------------------------
# 1. Write a Python program to print "Hello, World!" to the screen.
# 2. Write a program to take user input (their name) and display it on the screen.
# 3. Create a Python program to calculate the sum of two numbers.
# 4. Write a program to check if a number is even or odd.
# 5. Create a program that calculates the square of
# a number.
# 6. Write a Python program to find the maximum of two numbers.
# 7. Write a program that prints the numbers from 1 to 10.
# 8. Create a Python program to print the multiplication table of a given number.
# 9. Write a program to check if a given number is positive, negative, or zero.
# # 10. Create a program that calculates the factorial of a number.
# 10. Create a program that calculates the factorial of a number.
# 11. Write a Python program to check if a number is prime.
# 12. Create a program to swap the values of two variables.
# 13. Write a program to calculate the average of a list of numbers.
# 14. Create a program that finds the largest number in a list.
# 15. Write a Python program to reverse a string.
# 16. Create a program to find the length of a string.
# 17. Write a program to check if a string is a palindrome.
# 18. Create a program to count the number of vowels in a string.
# 19. Write a Python program to find the sum of all even numbers from 1 to 100.
# 20. Create a program to check if a given year is a leap year.
# 21. Write a program that generates a random number and asks the user to guess it.
# 22. Create a program that converts Fahrenheit to Celsius.
# 23. Write a Python program to calculate the area of a rectangle.
# 24. Create a program that counts the number of words in a sentence.
# 25. Write a program to find the common elements between two lists.
# 26. Create a program that sorts a list of numbers in ascending order.
# 27. Write a Python program to find the second largest element in a list.
# 28. Create a program that generates a simple calculator.
# 29. Write a program to check if a given string contains only digits.
# 30. Create a program to calculate the sum of all prime numbers from 1 to 100
# 31. Write a Python program to calculate the area of a circle.
# 32. Create a program that checks if a given number is a perfect square.
# 33. Write a program to find the square root of a number.
# 34. Create a program that generates a simple to-do list.
# 35. Write a Python program to find the LCM (Least Common Multiple) of two numbers.
# 36. Create a program to check if a string contains only alphabetic characters.
# 37. Write a program that calculates the power of a number (a^b).
# 38. Create a program to calculate the sum of all natural numbers up to a given N.
# 39. Write a Python program to find the factorial of a number using a loop.
# 40. Create a program to check if a string is a valid email address.'''

# 1.
# print("hello world")
# # 2.
# user=input("enter a name")
# print(user)
# 3
# a=int(input("enter a number"))
# b=int(input("enter second number"))
# print("sum :",a+b)
# def add(num1,num2):
#     return num1+num2;
# a =int(input("enter number"))
# b = int(input("enter second"))
# print('Sum of the numbers is : ',add(a,b))
# 4
# a=int(input("enter a number"))
# if a%2==0:
#     print(a,"is even")
# else:
#     print(a," is odd")

# 5
# a=int(input("enter a number"))
# print(a**2)
# num =int(input("enter a number"))
# print(f'square of {num} is {num**2}')
# 6
# num1 = int(input('enter the first number : '))
# num2 = int(input('enter the second number : '))
# if num1>num2:
#     print(f'{num1} is the maximum value')
# else:
#     print(f'{num2} is the maximum value')
# 7
# i=1
# while(i<=10):
#     print(i)
#     i+=1
# 9
# a=int(input("enter a number"))
# for i in (1,11):
#     print(f'{a} * {i} = {a * i}')


# num = int(input('Enter the number: '))
# for i in range(1, 11):
#     print(f'{num} * {i} = {num * i}')
#

# 10
# a=int(input("enter a number"))
# if a>0:
#      print(f'{a} is positive')
# elif a==0:
#      print(f'{a} is zero')
# else:
#      print(f'{a} is negative')
#
# a=int(input("enter a number"))
# i=1
# f=1
# while(i<=a):
#     f*=i
#     i+=1
# print(f)


# num=int(input("Enter a number: "))
# a=1
# for i in range(1,num+1):
#     a*=i
#
# print("Factorial of %d = %d"%(num,a))

# a=int(input("enter a number"))
# i=1
# f=1
# if a>0:
#     while (i <= a):
#         f *= i
#         i += 1
#     print(f)
# else:
#     print("number is not valid")
# 11
#
# lis=[12,11,5,8,5]
# print(f'list={lis}')
#
# i=len(lis)
# sum=0
# for i in lis:
#     sum+=i
# print(sum)
# print('avg of the list is :',sum/i)


# lis = [15,9,55,41,35,20,62,49]
# sum=sum(lis)
# length = len(lis)
# avg = sum/length
# print("Average of the list is :",avg)


# # 14
# lis=[52,8,5,8,5]
# a=0
#
# for i in lis:
#     if i>a:
#         a=i
# print(a)



# list = [5,2,33,75,84,356,2,6,3]
# list.sort()
# print(list)
# print("Largest element in the list is :",list[-1])









# 12

# a=10
# b=12
# c=b
# b=a
# a=c
# print(a,b)



# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# print("a=%d  b=%d"%(a,b))
#
# temp=a
# a=b
# b=temp
# print(f"after swap a={a} & b={b}")

# 13.
# lis=[1,8,6,99,45]
# l=len(lis)
# # print(l)
# sum=0
# for i in lis:
#      sum+=i
# # print(sum)
# avg=sum/l
# print(f'avg number of list is {avg}')

# # 14.
# lis=[1,8,6,99,45]
# lis.sort()
# print("largest number is ",lis[-1])

# 15.
# x=input("enter a string")
# rev=x[::-1]
# print(rev)





# 16.
#
# x=input("enter a string")
# count=0
# for i in x:
#     count+=1
# print(count)


# 17.

# x=input("enter a string")
# rev=x[::-1]
#
# if x==rev:
#     print("pallindrome")
# else:
#     print("its not")

# str = input("Enter a string :")
# reverse = str[::-1]
# if reverse==str:
#     print(str,"is palindrome")
# else:
#     print(str,"not palindrome and its reverse is",reverse)

# # 18.
#
# str = input("Enter a string :")
# x=['a','e','i','o','u']
# count=0
# for i in str:
#     if i in x:
#         count+=1
# print(count)


# 19.
# count=0
# for i in range (1,101):
#     if i%2==0:
#         count+=i
# print(count)
# 20.
# year=int(input("enter year"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print('not a leap year')


# 31. Write a Python program to calculate the area of a circle.
# 32. Create a program that checks if a given number is a perfect square.
# 33. Write a program to find the square root of a number.
# 34. Create a program that generates a simple to-do list.
# 35. Write a Python program to find the LCM (Least Common Multiple) of two numbers.
# 36. Create a program to check if a string contains only alphabetic characters.
# 37. Write a program that calculates the power of a number (a^b).
# 38. Create a program to calculate the sum of all natural numbers up to a given N.
# 39. Write a Python program to find the factorial of a number using a loop.
# 40. Create a program to check if a string is a valid email address.
# 41. Write a program to reverse a list in Python.
# 42. Create a program to check if a given number is a palindrome.
# 43. Write a Python program to count the number of words in a paragraph.
# 44. Create a program to find and print the Fibonacci sequence up to N terms.
# 45. Write a program to check if a list is sorted in ascending order.
# 46. Create a program that calculates the area of a triangle.
# 47. Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.
# 48. Create a program to print the ASCII value of a character.
# 49. Write a program to find and print all prime numbers up to N.
# 50. Create a program that converts a decimal number to binary.
# 51. Write a Python program to find the minimum and maximum elements in a list.
# 52. Create a program to count the number of uppercase and lowercase letters in a string.
# 53. Write a program to reverse the order of words in a sentence.
# 54. Create a program to calculate the sum of a geometric series.
# 55. Write a Python program to calculate the volume of a sphere.
# 56. Create a program that generates a random password of a given length.
# 57. Write a program to find and print the factors of a number.
# 58. Create a program to check if a list contains duplicate elements.
# 59. Write a Python program to find and replace a word in a string.
# 60. Create a program that checks if a given string is a pangram (contains all alphabets).


# 31
# r=int(input("enter a radious"))
# area=3.14*(r**2)
# print("area of circle : ",area)
# 32
# n=int(input("enter a number"))
# a=n**.5
# if n==a*a:
#     print("perfect square")
# else:
#     print("not a perfect square")

# 33.
# n=int(input("enter a number"))
# print(f" {n} of square root is :",n**.5)
#
# a=[]
# while True:
#    print("1 for add","\n2 for display","\n 3 for for remove")
#    choice=int(input("choice"))
#    if choice==1:
#          n = int(input("enter elements"))
#          for i in range(n):
#            el = input("type")
#            a.append(el)
#    elif choice == 2:
#        print(a)
#    elif choice == 3:
#
#         a.pop()
#         print("removed")
#         print(a)
#    else:
#        print(("correct"))
# #        break
#
# num1 = int(input('enter the num 1: '))
# num2 = int(input('enter the num 2: '))
# for i in range((num1*num2),1,-1):
#     if num1%i==0:
#         if num2%i==0:
#             x1 = num1//i
#             x2 = num2//i
#             if (x1*num2)==(x2*num1):
#                 print(f'LCM of {num1} and {num2} is {x1*num2}')
#                 break
#

# 36

# a=input("enter a word")
# if a.isalpha():
#     print("yes")
# else:
#     print("no")
# 37
# a=int(input("enter num "))
# b=int(input("num "))
# print(f" {a}^{b} :",a**b)

# 38.

# n=int(input("enter  a number"))
# sum=0
# for i in range(0,n):
#     sum+=i
# print(f" sum of {n} natural is : ",sum)
#
# 39

# f=1
# n=int(input("enter  a number"))
# for i in range (1,n+1):
#     f*=i
# print(f" factorial {n} is :",f)
# 40
# a=input("email")
# b=a.split('.')
# if '@' in b[0] and 'com' in b[1] and '.' in a:
#     print("valid")
# else:
#     print("not")


a=[1,8,5,4]
rev=[]
for i in a:
    




