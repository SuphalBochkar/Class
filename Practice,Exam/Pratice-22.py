# To Find Power From Input
    # a = input()                    #string
    # ex = pow(int(a[0]),int(a[-1])) #to find Power
    # print((ex),(ex % 2 == 0))      #it print's in boolean
# To find Equal str from 2 inputs
    # a = str(input())
    # b = str(input())
    # c = len(b)
    # print(a[0] == b[-1],c)
#Fibonacci
n1 = int(input("enter first: "))
n2 = int(input("enter second: "))
noft = int(input("No of terms u need: "))
print(n1,n2)
while(noft-2):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)
    noft = noft -1
n1=0
n2=1
print(n1,n2)
n3=n1+n2
print(n3)
# Checking common letters from input
    # a = str(input())
    # b = str(input())
    # if(a[-1] in b and a[-2] in b):
    #     print("hiiiii")
    # print(a[-1] in b and a[-2] in b)
# Printing List Items
    # list = [10,11,12,13,14]
    # length = len(list)
    # i=0
    # while i<length:
    #     print(list[i])
    #     i  = i+1
    # for i in list:
    #         print(i)
    # for j in "Suphal":
    #     print(j)
#Adding List Items
    # x = [9,4,3,8,7,2,6,1,5]
    # length=len(x)
    # sum = 0
    # i=0
    # while i<len(x):
    #     sum = sum +x[i]
    #     i=i+1
    # print("the sum of list is ", sum)

