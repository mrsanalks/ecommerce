
# Write a Python program to calculate the discount percentage based on the purchase amount. If the purchase amount is greater than or equal to 1000, apply a 10% discount. If the amount is less than 1000, apply a 5% discount. Print the final discounted amount.

purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount >= 1000:
    discount = purchase_amount*10/100
    discounted_amount = purchase_amount - (purchase_amount * discount)
    print("Discounted amount:",discounted_amount)
else:
    discount =purchase_amount*5/100
    discounted_amount = purchase_amount - (purchase_amount * discount)
    print("Discounted amount:",discounted_amount)

    Given
    the
    age and height
    of
    a
    person, write
    a
    Python
    program
    to
    determine if the
    person is eligible
    for a roller coaster ride.To be eligible, the person must be at least 10 years old and have a height of 130 cm or more.


age = int(input("Enter your age: "))
height = float(input("Enter your height (in cm): "))

if age >= 10 and height >= 130:
    print("You are eligible for the roller coaster ride!")
else:
    print("Sorry, you are not eligible for the roller coaster ride.")
