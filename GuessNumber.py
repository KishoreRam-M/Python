import random

print("Welcome to Number Guessing Game!")

upto = int(input("Enter the maximum number to guess: "))
guess = int(input(f"Enter your guess (between 1 and {upto}): "))

def guessNumber(upto, guess):
    number = random.randint(1, upto)
    print(f"Random number was: {number}")
    if guess == number:
        print(" You Won!")
    else:
        print(" You Lose!")

guessNumber(upto, guess)
