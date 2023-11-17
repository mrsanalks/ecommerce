# unit=int(input("enter unit"))
#
# if unit<100:
#     print("zero")
# elif unit > 100 and unit<=200:
#     amount=(unit*5)
#     print(amount)
# elif unit>200:
#     amount=(100*5)+((unit-200)*10)
#     print(amount)

n=int(input("enter a number "))
for i in range (n):
   for j in range (0,i+1):
      print(i+1,end=" ")
print()
