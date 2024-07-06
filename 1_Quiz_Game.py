print("Welcome to the Game!")
initiate=input("Do you want to begin? ")
if initiate.strip().lower() not in ['yes','y']:
    quit()

print("\nAlright, let's begin :)")
score=0

answer=input("\nWhat does 'CPU' stand for? ")
if answer.strip().lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer=input("\nWhat does 'RAM' stand for? ")
if answer.strip().lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer=input("\nWhat does 'OS' stand for? ")
if answer.strip().lower() == "operating system":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer=input("\nWhat does 'UI' stand for? ")
if answer.strip().lower() == "user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer=input("\nWhat does 'GPU stand for? ")
if answer.strip().lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print(f"\nWell Played!\nYour final score is {score}/5\n", sep="")