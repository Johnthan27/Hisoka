import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []

# For loop for letters
for _ in range(nr_letters):
    password.append(random.choice(letters))

# For loop for symbols
for _ in range(nr_symbols):
    password.append(random.choice(symbols))

# For loop for numbers
for _ in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the password to randomize the order
random.shuffle(password)

# Convert the password list to a string
password_str = ''.join(password)

# Print the generated password
print(f"Your generated password is: {password_str}")
