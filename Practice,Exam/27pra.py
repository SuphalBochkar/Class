# Reverse Number
numb = int(input("Enter the number to be reversed:"))
rev = 0

while (numb>0):
    # logic
    rem = numb%10
    rev = (rev*10)+rem
    numb = numb // 10 
    print(rev)   

