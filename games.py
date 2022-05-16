import random
a=int(input("enter a lower limit"))
b=int(input("enter a upper limit"))
guess=0
n=random.randint(a,b)
str1=str(n)

for i in range(1,6):
    c=int(input("enter a  number between the limits"))
    str2=str(c)
    if(str1==str2):
        print("matched")
        guess=1
        break
    else:
        q=list(set(str1) & set(str2))
        # for i in q:
        z=len(q)
        if(z>0):
         print("you are closer")
        else:
            guess=0
            print("failed")
if(guess==0):
    print("Game Over")
    print("Answer = ",n)
