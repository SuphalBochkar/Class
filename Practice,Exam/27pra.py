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
num = int(input("Enter Number:"))
count = 0
i = 1
while 1:    
    while i <= num:
        if num % i ==0:
            count = count +1
        i = i+1
    if count==2:
        print("Its a Prime :) ")
    else :
        print ("Its not Prime :(")
    
    # x=str(input())
    # if x == "exit" or "Exit":
    #     break

