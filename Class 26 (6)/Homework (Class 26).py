import random

def generate_password(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # Lowercase, uppercase, and digits
    password = ''.join(random.choice(characters) for _ in range(length))  # Generate the password
    return password


while True:
    length = int(input("Enter the password length (between 6 and 20): "))
    if 6 <= length <= 20:
        break
    else:
        print("Invalid input. Please enter a length between 6 and 20.")

print(generate_password(length))