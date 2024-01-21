# The magician's secret number
secret_number = 42

# Keep prompting the user until they guess the correct number
while True:
    # Ask the user to enter an integer number
    user_guess = int(input("Guess the secret number: "))

    # Check whether the user's guess matches the secret number
    if user_guess == secret_number:
        print("Well done, muggle! You are free now.")
        break  # Exit the loop if the guess is correct
    else:
        print("Ha ha! You're stuck in my loop!")
