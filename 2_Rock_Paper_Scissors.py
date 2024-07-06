import random

print("Welcome to the Game!")
initiate=input("Do you want to begin? ")
if initiate.strip().lower() not in ['yes','y']:
    quit()

print("\nAlright, let's begin :)")
user_score = 0
comp_score = 0
choices= ["rock", "paper", "scissors"]

while True:
    user_choice=input("\nChoose your weapon: rock / paper / scissors (or) q to Quit: ").strip().lower()

    if user_choice == "q":
        break
    elif user_choice not in choices:
        continue
    else:
        comp_choice=random.choice(choices)
        print(f"\nThe computer chose: {comp_choice}!")

        if user_choice==comp_choice:
            print("TIE!")
        else:
            if user_choice=="rock" and comp_choice=="scissors":
                print("You Won! :)")
                user_score+=1

            elif user_choice=="paper" and comp_choice=="rock":
                print("You Won! :)")
                user_score+=1

            elif user_choice=="scissors" and comp_choice=="paper":
                print("You Won! :)")
                user_score+=1
            else:
                print("You Lost! :(")
                comp_score+=1

print(f"\nFINAL SCORES:\nYour Score: {user_score}")
print(f"Computer's Score: {comp_score}\n")

if user_score>comp_score:
    print("You are the Winner! :)")
elif user_score==comp_score:
    print("It was a TIE!")
else:
    print("The computer is the Winner! :(")
print("Goodbye!\n")
