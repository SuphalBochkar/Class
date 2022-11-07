#Rock,Paper,Scissors
import random
print("Welcome to RPS")
uc = input("Enter either r or p or s\n")
cc = ["r","p","s"]
cs = random.choice(cc)
print(f'user choice is {uc} and pc choice is {cs}')
if uc==cs:
    print("its draw")
elif uc=="r" and cs =="p":
    print("you lost")
elif uc=="r" and cs =="s":
    print("you won")
elif uc=="p" and cs =="s":
    print("you lost")
elif uc=="p" and cs =="r":
    print("you won")
elif uc=="s" and cs =="r":
    print("you lost")
elif uc=="s" and cs =="p":
    print("")
else :
    i=1
    while i<20:
        print("!!!!!! Wrong Input!!!!! ")
        i=i+1


