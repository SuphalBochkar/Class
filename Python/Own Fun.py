# ----------07/11/22-----------
# 1. Defining 
    # def pr_int():
    #     print("Making Own Functions")  #Defining A function
    # pr_int()     #CAlling Of Function
# 2.Paramterised
# Paramterised function , function capable of accepting value
    # def pr(name):
    #     print("My name is "+name)
    # pr("Suphal")
    
    # def pr_int(first_name,last_name):
    #     print("This is "+first_name+last_name)
    # pr_int("Suphal","Bochkar")
# More Variable while Calling
# tuple
    # def pr(*name):
    #     for i in range(4):
    #         print("My name is "+name[i])
    # pr["suphal","bochkar","qwerty"]
# Dictionary
    # def pr(name1,name2,name3):
    #     print("My name is "+name3)
    # pr(name1="last",name2="shadow",name3="67")
# Loop in DEF
    # def pr(name):
    #     for i in name:
    #         print(i)
    # name=["last","Shadow","67"]
    # pr(name)
    
# Return
    # def pr(n):
    #     return n*2
    # print(pr(7))

# Recursion Function calls itself to perform task
    # def factorial(x):
    #     if x==1:
    #         return 1
    #     else:
    #         return (x*(factorial(x-1)))
    # print(factorial(4))
#Reverse A Number
    # n=int(input())
    # i=0
    # while n>0:
    #     r=n%10
    #     i=(i*10)+r
    #     n=n//10
    # print(i)