import random

print("NUMBER GUESSING GAME")
print("I am thinking of a number between 1 and 100")

secret_number = random.randint(1, 100)
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low 🔽 Try again")
    elif guess > secret_number:
        print("Too high 🔼 Try again")
    else:
        print(f"Correct! You guessed it in {attempts} attempts")

input("Press Enter to exit...")
