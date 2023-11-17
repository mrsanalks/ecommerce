import re
# rule="[A-Za-z]+"
# word=input("enter name")
# match=re.fullmatch(rule,word)
# if match:
#     print("valid name")
# else:
#     print("invalid name")


# name should start with uppercase
# lowercase,spacee
# # 7-8
# rule="^[A-Z[a-z\s]{6,9}"
# word=input("enter name")
# match=re.fullmatch(rule,word)
# if match:
#     print("valid name")
# else:
#     print("invalid name")

# the name should only start with A ,B C
# followed by lower cases
# # number should be icluded or not iclided
# import re
import re
# rule="^[ABC][a-z]+[0-9]*"
# word=input("enter name")
# match=re.fullmatch(rule,word)
# if match:
#     print("valid name")
# else:
#     print("invalid name")
# rule="^[9876][0-9]{9}"
# number=input("enter number")
# match=re.fullmatch(rule,number)
# if match:
#     print("valid number")
# else:
#     print("invalid number")

# rule="^[+][9][1][9876][0-9]{9}"
#
# number=input("enter number")
# match=re.fullmatch(rule,number)
# if match:
#     print("valid number")
# else:
#     print("invalid number")

#
# import re
# rule="^[A-C][a-z]+([^0-9]|[0-9]{1,2})"
# word=input("enter name")
# match=re.fullmatch(rule,word)
# if match:
#      print("valid name")
# else:
#     print("invalid name")



#
# # email validation
# rule="^[a-z]+[0-9]*[*_]?[a-z0-9]*[@][g][m][a][i][l][.][c][o][m]"
# word=input("enter name")
# match=re.fullmatch(rule,word)
# if match:
#      print("valid email name")
# else:
#     print("invalid email name")
#
#


# # rule="^[0-9]{1,2}[/-]+[0-9]{1,2}[/-]+[0-9]{1,4}"
# rule=r"([0-9]{1,2}[\\][0-9]{1,2}[\\][0-9]{1,4}|[0-9]{1,2}[-][0-9]{1,2}[-][0-9]{4})"
# date=input("enter date")
# match=re.fullmatch(rule,date)
# if match:
#      print("valid dob")
# else:
#     print("invalid dob")
#







# registration and login using regex
# enter name:
# enter email:
# enter phone:
# enter pswrd:




rule="[A-Za-z]+"
word=input("enter name")
email=input("enter email")
rulea="^[a-z]+[0-9]*[*_]?[a-z0-9]*[@][g][m][a][i][l][.][c][o][m]"
ruleb="^[+][9][1][9876][0-9]{9}"
number=input("enter number")
match=re.fullmatch(rule,word,email,rulea,ruleb,number)
if match:
    print("reg success")
    print("enter email")


















