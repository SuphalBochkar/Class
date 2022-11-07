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
def pr(name):
    for i in name:
        print(i)
name=["last","Shadow","67"]
pr(name)
