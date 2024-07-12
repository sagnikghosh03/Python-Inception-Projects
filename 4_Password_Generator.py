import random
import string

def main():
    length=int(input("\nWhat should be the length of the Password? "))
    has_num=input("Do you want to include Numbers (y/n)?").strip().lower() =='y'
    has_special=input("Do you want to include Special Characters (y/n)?").strip().lower() == 'y'

    letters=string.ascii_letters
    num=string.digits
    special=string.punctuation

    characters=letters

    if has_num:
        characters += num

    if has_special:
        characters += special

    pwd=""    
    for i in range(length):
        pwd += random.choice(characters)

    print("\nYour Password:", pwd)

    
if __name__=="__main__":
    main()
