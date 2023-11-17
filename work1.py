lis=["ayshu","lachu","farzu","shigin","sanalks"]
def longest_word(lis):
    longest_word=""
    lengthoftheword=0
    for i in lis:
        if len(i)>lengthoftheword:
            longest_word=i
            lengthoftheword=len(i)
    print("longest word from given list is :",longest_word)
    print("length of the word from the list :",lengthoftheword)
longest_word(lis)


word=input("enter a word ")
strng=""
for i in word:
    if word.index(i)%2==0:
        strng+=i
print(strng)

li=['a','b','c','d']
dic={}
for i in li:
    key=i
    value=li.index(i)
    dic.update({key:value})
print(dic)

def calculate_digit_sums(numbers):
    digit_sums = []
    for number in numbers:
        digits = [int(digit) for digit in str(number)]
        digit_sum = sum(digits)
        digit_sums.append(digit_sum)
    return tuple(digit_sums)

my_tuple = (1234, 789, 963,456)
result_tuple = calculate_digit_sums(my_tuple)
print(result_tuple)





word=input("enter a word")
if len(word)>0:
    first=word[0]
    mid=word[1:-1]
    last=word[-1]
    new=last+mid+first
    print(new)
else:
    print("enter any word")


