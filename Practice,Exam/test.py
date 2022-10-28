x=int(input("1st:"))
y=int(input("2nd:"))
z=int(input("No of:"))
while(z-1):
    a=x+y
    x=y
    y=a
    print(a)
    z=z-1
