# import re
# str="this is"
# pattern=input("enter word")
# x=re.findall(pattern,str)
# print(x)

# #
# import re
# rule="[A-Za-z]+"
# word=input("enter name")
# match=re.findall(word,rule)
# print(match)

# str="number is 856112 and 9556322"
# pattern="\d+"
# x=re.findall(pattern,str)
# print(x)

# str="number is 856112 and 9556322"
# pattern="\D+"
# x=re.findall(pattern,str)
# print(x)

# import re
# str="number is 856112 and 9556322"
# pattern="\w+"
# x=re.findall(pattern,str)
# print(x)

# ###############search option########
import re
str="hello world"
word=input("enter a word")
x=re.search(word,str)
print(x)