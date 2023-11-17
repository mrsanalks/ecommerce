# # # # width = 10
# # # # height = 5
# # # # print(width * height)
# # #
# # # #
# # # #
# # # # sentence = "The quick brown fox jumps over the lazy dog"
# # # # print(len(sentence))
# # #
# # # #
# # # # list_of_numbers = [1, 2, 3, 4, 5]
# # # # # print(len(list_of_numbers))
# # # # num = 6
# # # # print(num ** 2)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # greeting = "Hello, how are you doing?"
# # # print(greeting + " ",name)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # #
# # # # fv_color="red"
# # # # print("my fav color is ",fv_color)
# # #
# # # num1=5
# # # num2 = 3
# # # print("Sum:", num1 + num2)
# # # print("Difference:", num1 - num2)
# # # # print("Product:", num1 * num2)
# # # # print("Quotient:", num1 / num2)
# # # sentence1='cricket'
# # #
# # # sentence2 = "It's my passion."
# # # print(sentence1 + " " + sentence2)
# # #
# # # #
# # # my_list.append(6)
# # # print(my_list)
# # #
# # # #
# # # string1 = "Hello, world!"
# # # for char in string1:
# # #     print(char)
# # #
# # #
# # # num4 = 2
# # # num5 = 4
# # # while num4 < num5:
# # #     print(num4)
# # # #     num4 += 1
# # #
# # # string2 = "h"
# # # try:
# # #     integer_value = int(string2)
# # #     print(integer_value)
# # # except ValueError:
# # #     print("Conversion to integer failed.")
# #
# #
# #
# # #
# # #
# # # name = input("What is your name? ")
# # # if len(name) < 5:
# # #     print("Hello, ",name)
# # # else:
# # #     print("Greetings, ",name)
# #
# #
# # #
# # # year=int(input("enter a year"))
# # #    if year %== 4:
# # #      if year % ==100:
# # #          if year%!=400:
# # # #          print("leap yesar")
# # # # else:
# # # #     print("not")
# # # #
# # # #
# # #
# # #
# # #
# # # year = int(input("Enter a year: "))
# # # if year % 4 == 0:
# # #     if year % 100 == 0:
# # #         if year % 400 == 0:
# # #             print(year, "is a leap year.")
# # #         else:
# # #             print(year, "is not a leap year.")
# # #
# # #     else:
# # #         print(year, "is a leap year.")
# # # else:
# # # #     print(year, "is not a leap year.")
# # # num1 = float(input("Enter the first number: "))
# # # num2 = float(input("Enter the second number: "))
# # # num3 = float(input("Enter the third number: "))
# # # if num1 >= num2 and num1 >= num3:
# # #     print(num1 + max(num2, num3))
# # # elif num2 >= num1 and num2 >= num3:
# # #     print(num2 + max(num1, num3))
# # # else:
# # #     print(num3 + max(num1, num2))
# # #
# # month = input("Enter a month: ").lower()
# # day = int(input("Enter a day: "))
# # if month in ["january", "february", "march"]:
# #     season = "winter"
# # elif month in ["april", "may", "june"]:
# #     season = "spring"
# # elif month in ["july", "august", "september"]:
# #     season = "summer"
# # else:
# #     season = "fall"
# # if month == "march" and day >= 20:
# #     season = "spring"
# # elif month == "june" and day >= 21:
# #     season = "summer"
# # elif month == "september" and day >= 22:
# #     season = "fall"
# # elif month == "december" and day >= 21:
# #     season = "winter"
# # print("The season is", season)
#
#
#
# age = int(input("Enter your age: "))
#
# if age < 18:
#     grade_level = int(input("Enter your grade level: "))
#     if grade_level <= 8:
#         print("You are not eligible for a driver's license.")
#     else:
#         print("You are eligible for a driver's permit.")
# else:
#     print("You are eligible for a driver's license.")






# Write a program that prompts the user to enter a number between 1 and 10. If the number is less than 1 or greater than 10, print an error message. If the number is between 1 and 10, prompt the user to enter another number. If the second number is greater than or equal to the first number, print "The second number is greater than or equal to the first number." If the second number is less than the first number, print "The second number is less than the first number.
a=int(input('enter a number'))
b=int(input("enter second number"))
if a <1 or a>=10:
 print('error')
    if a>=1 and a<=10:
        print(b)
if b>=a:
     print("second is greater")
else:
     print("first number is greater")








































