# # set={'ab','22','ff'}
# # print(set)
# # # find length
# # count=0
# # for i in set:
# #     count+=1
# # print(count)
# # # add()method:it is used to add one item
# # set.add("d")
# # print(set)
# # # create an empty set add elements into the set
# #
# # a=set({})
# # n=int(input("enter number of elements"))
# # for i in range(0,n):
# #     b=input("enter elements ")
# #     a.add(b)
# # print(a)
#
#
# lis=['a','a','b','b','c','c','c']
#
# li=set(lis)
# x=list(li)
# x.sort()
# print(x)
#
# # update method
# # used to add items from another set
#
#
# s1={'h','g''k','j'}
# s1.update(x)
# print(s1)
# s3=[1,2,3,]
# s1.update(s3)
# print(s1)
# s4=(6,7,8)
# s1.update(s4)
# print(s1)
# # remove method
# # s1.remove("h")
# # print(s1)
# # s1.discard('j')
# # print(s1)
#
# s1.pop()
# print(s1)


#
# alphabets={'a','b','c','d'}
# while True:
#     choice=input("do you want to remove element from the set")
#     if choice=="yes":
#         element=input("enter the element to remove")
#         alphabets.remove(element)
#         print(alphabets)
#     elif choice=="no":
#         print("exit")
#         break
# advanced by chat gpt

# create a set of alphabets
# alphabets_set = set('abcdefghijklmnopqrstuvwxyz')
#
# # loop until the user chooses to end
# while True:
#     # ask the user if they want to remove an element
#     answer = input("Do you want to remove an element from the set? (y/n): ")
#     if answer.lower() == 'y':
#         # ask the user to enter the element they want to remove
#         element = input("Enter the element you want to remove: ")
#         # try to remove the element from the set
#         try:
#             alphabets_set.remove(element)
#             print(f"{element} removed from the set.")
#         except KeyError:
#             print(f"{element} is not in the set.")
#     elif answer.lower() == 'n':
#         break
#     else:
#         print("Invalid input. Please enter 'y' or 'n'.")


#
# x={'a',"b","c"}
# y={"b","d"}
# x.intersection_update(y)
# print(x)
#
#

#
# x={'a',"b","c"}
# y={"b","d"}
# x.symmetric_difference_update(y)
# print(x)
# frozenset
#
# list={1,2,3}
# x=frozenset(list)
# x.append("a")
# print(x)
#
#




