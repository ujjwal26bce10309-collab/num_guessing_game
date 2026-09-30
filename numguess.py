import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        # Ask the user for their guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess against the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid whole number:")
