import random

print("Welcome to the Game!")
initiate=input("Do you want to begin? ")
if initiate.strip().lower() not in ['yes','y']:
    quit()

print("\nAlright, let's begin :)\n")

comp_choice=random.randint(1,100)
u_i=-1
guess_num=1
print("Choose a number between 1 and 100!")

while (u_i != comp_choice):
    u_i=int(input("Guess the number: "))
    if u_i<comp_choice:
        print("\nHigher Number Please!")
        guess_num +=1
    elif u_i>comp_choice:
        print("\nLower Number Please!")
        guess_num +=1

print(f"\nWell Played!\nThe Computer chose the number '{comp_choice}'. \nYou guessed it right in {guess_num} attempts!\n")