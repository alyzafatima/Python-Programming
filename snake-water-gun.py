import random
import os
k=0
j=0

n=int(input("\n\n \t\tHow many rounds ypou want to play : "))
name=input("\n\t\t\tEnter your name : ")
os.system("pause")
os.system('CLS')
i=0
while(k<n):
    print("\t\t\t\t ROUND NO - ",k+1)
    list1=["water", "snake", "gun"]
    a=random.choice(list1)
    print("Choose one - water - snake - gun ")
    b=input()
    if b=="snake":
        if a=="snake":
            print("-DRAW-")
            print("Other user select : ",a)
            print("\n")
        elif a=="water":
            print("-YOU WIN-")
            print("Other user select : ",a)
            print("\n")
            i=i+1
            
        else:
            print("-YOU LOSE-")
            print("Other user select :",a)
            print("\n")
            j=j+1
    elif b=="water":
        if a=="water":
            print("-DRAW-")
            print("Other user select : ",a)
            print("\n")
        elif a=="gun":
            print("-YOU WIN-")
            print("Other user select : ",a)
            print("\n")
            i=i+1
        else:
            print("-YOU LOOSE-")
            print("Other user select : ",a)
            print("\n")
            j=j+1
    elif b=="gun":
        if a=="gun":
            print("-DRAW")
            print("Other user select : ",a)
            print("\n")
        elif a=="water":
            print ("-YOU LOOSE-")
            print("Other user select : ",a)
            print("\n")
            j=j+1

        else:
            print("-YOU WIN-")
            print("Other user select : ",a)
            print("\n")
            i=i+1
    k=k+1
    os.system("pause")
    os.system('CLS')

if i>j:
    print("\t\t",name, "You are the winner!!!")
elif i==j:
    print("\t\t -GAME DRAW-")
else:
    print("\t\tOther user is winner ")
print("\t\t",name," you win ",i,"rounds")
print("\t\tOther user win ",j,"rounds")