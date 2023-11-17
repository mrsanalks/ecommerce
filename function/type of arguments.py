# # # def add(a,b=1):
# # #     print(a+b)
# # # add(7)
# # # add(1,2)
# #
# #
# #
# # def multiply(a,b,c=1,d=1):
# #     z=a*b*c*d
# #     print(z)
# # multiply(1,2,3)
# # multiply(1,2,3,4)
# # multiply(1,2)
# #
# # def largest(a,b,c,d):
# #     if a>b and a>c and a>d:
# #         print(a)
# #     elif b>c and b>d and b>a:
# #         print(b)
# #     elif c>d and c>b and c>a:
# #         print(c)
# #     elif d>c:
# #         print(d)
# #
# # largest(2,3,43,55)
# # largest(1,2,3)
#
#
#
# # keyword_arguments
# #
# # def name(first_name,middle_name,last_name):
# #     print(first_name,middle_name,last_name)
# # name(middle_name="san",first_name="ayshu",last_name="farzu")
#
#
#
# # arbitrage
# #
# # def add(*a):
# #     print(a)
# # add(1,2,3,4)
# # # out will be a tupple
#
#
# #
# # def add(*a):
# #     b=0
# #     for i in a:
# #       b+=i
# #
# #     print(b)
# # add(1,2,3,4)
#
#
#
# def multiple(*a):
#     b=1
#     for i in a:
#       b*=i
#
#     print(b)
# multiple(1,2,3,4)
# multiple(1,2,3)
# using arbirtrage find largest number without function

#
# def largest(*a):
#     b=0
#
#     for i in a:
#         if i>b:
#             b=i
#     print('%d is the largest'%b)
# largest(2,5,15,7,9)
# largest(25,15,8,75,2)
# largest(250,45,75,14,65,500)
#


# arbitary keyword argument
#
# def name(**kwargs):
#     for i,j in kwargs.items():
#
#      print(i,j)
#
# name(firstname="san",lastname="ayshu",middle="farzu",phone=98745631)

# we will get dictionary so we have to change through iteration












