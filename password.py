import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

choice = input("Do you want to (1) create your own password or (2) generate one? Enter 1 or 2: ")

if choice == '1':
    password = input("Enter your own password: ")
    print("Your password is:", password)
    print("Password Length:", len(password))
elif choice == '2':
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a number.")
else:
    print("Invalid choice.")
