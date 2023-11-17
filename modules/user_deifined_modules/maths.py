# function with arg and return tye
#
# write a function add numbers with a return type?
#  def add(arg)
#
#
# rev number()
#
# armsstrong()






def add(*a):
    b=0
    for i in a:
        b+=i
    return(b)


def rev(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return(rev)
#
# def rev(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n//=10
#     return(rev)
# #



#
def armstrng(n):

    copy=n
    armstrng=0

    while n!=0:
        reminder=n%10
        armstrng+=reminder**3
        n//=10

    if copy==armstrng:
        return("armstrong")
    else:
        return("not")




