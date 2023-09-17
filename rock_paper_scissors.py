'''
Rock, Paper, Scissors:

Description: Implement the classic Rock, Paper, Scissors game where the user plays against the computer. 
The user chooses one of the three options, and the computer also makes a random choice.
Purpose: This project involves user input, randomization, and basic conditional statements.

A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors")
but will lose to one who has played paper ("paper covers rock"); 
a play of paper will lose to a play of scissors ("scissors cuts paper"). 
If both players choose the same shape, the game is tied and is usually replayed to break the tie.

'''

import random

options = ['rock', 'paper', 'scissors']

while True:

    user_choice = input("\nEnter your choice between 'rock, paper, scissors' or type 'quit' to quit: ").lower()
    computer_choice = random.choice(options)
    
    print(f"Computer's choice: {computer_choice}")
    print(f"Your choice: {user_choice}")

    if user_choice not in options:
        print("Invalid choice, try again")
        continue

    if user_choice == "quit":
        breaks

    elif computer_choice == user_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
         
         print("You win!")

    else:
        print("Computer Wins")