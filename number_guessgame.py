
import random
x=random.randint(1,200)
z=0

print("this is the word guessing game entering the right number will give you score")
print("you will get three chance")
y=int(input("enter the number"))

if y==x:
    print("come..on you got it , you are too brilliant")
elif y>x:
        print(" high")
else:
        print(" small")

while z!=x:
     z=int(input("enter the number again"))
     if z==x:
         print("wowwwwwww!")
         print("you win",end="")
         print("you got 1000 points")

         break

     elif z<x-10:
         print("too small")

     elif z>=x-5 and z<=x-1:
         print("close")

     elif z>=x+1and z<=x+5:
         print("little high")

     elif z>x+10:
         print("too high")

     else:
         print("wrong number")