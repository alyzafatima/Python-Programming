import random
num=random.randint(0,20)
i=0
print("You have only five chances to guess exact number (between 0 to 20" )
while (i<5):
    i=i+1
    n=int(input("Guess the number : "))
    if n<num:
        print("\nYou Guess little low")
        print(5-i,"attempts left\n")
    elif n>num:
        print("\nGuess little high")
        print(5-i,"attempts left\n")
    elif n==num:
        print("\nCongratulations you guess the correct number !!\n")
        break
if n!=num and i==5:
    print("\n!!! YOU LOSE :( TRY AGAIN !!!\n")
    print("correct number was ", num)