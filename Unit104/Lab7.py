import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

# Set the maximum number of tries
max_tries = 3

# Loop for the number of allowed tries
for current_try in range(1, max_tries + 1):
    # Get the user's guess
    user_guess = int(input("Guess the number between 1 and 20: "))
    
    # Check if the guess is correct
    if user_guess == secret_number:
        print(f"Yes! You guessed it in {current_try} {'try' if current_try == 1 else 'tries'}.")
        break
    else:
        # Provide a hint whether the number is higher or lower
        print("Try again. The number is higher." if user_guess < secret_number else "Try again. The number is lower.")
else:
    # If the loop completes without a correct guess
    print(f"Sorry, you couldn't guess the number. The correct number was {secret_number}.")
