'''
Guess the Number:

Description: In this game, the computer generates a random number, and the user must guess it.
The computer provides hints to guide the user.
Purpose: This project introduces random number generation, user input handling, and conditional statements.
'''

import random

random_number = random.randint(1,50)

tries = 0


print("\nWelcome to the Guess the Number game!\n")

print("I'm thinking of a number between 1 and 50. Can you guess it?\n")

while True:
    user_guess = int(input("Guess a number between 1 and 50: "))

    if user_guess:
        tries += 1

    if user_guess < random_number:
        print("\nToo low, guess a higher number")

    elif user_guess > random_number:
        print("\nToo high, guess a lower number")

    else:
        print(f"You guessed right after {tries} tries, {user_guess} is correct!")
        break