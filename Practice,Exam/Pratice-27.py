# Reverse Number
    # numb = int(input("Enter the number to be reversed:"))
    # rev = 0
    # while (numb>0):
    #     # logic
    #     rem = numb%10
    #     rev = (rev*10)+rem
    #     numb = numb // 10 
    #     print(rev)   
# Prime Numbers
    # num = int(input("Enter Number:"))
    # count = 0
    # i = 1
    # while 1:    
    #     while i <= num:
    #         if num % i ==0:
    #             count = count +1
    #         i = i+1
    #     if count==2:
    #         print("Its a Prime :) ")
    #     else :
    #         print ("Its not Prime :(")
    # x=str(input())
    # if x == "exit" or "Exit":
    #     break
# DataTypes: Dictionary
# ordered , changable, no dublicate
# works on the concept of key and value
a={"name":"Suphal","company":"cipherschools","college":"LPU"}
# print(a)
print(a["name"])
a["degree"]=["engineering"]
print(a.keys())
if "name" in a:
    print("its therr")
