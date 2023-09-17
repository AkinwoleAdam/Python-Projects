'''Project 16: Random Quote Generator

Description: Develop a program that displays random quotes when the user runs it.
Store a collection of quotes, and randomly select and present one each time the program is executed.
Purpose: This project involves storing and retrieving data (quotes) and working with random selection.

'''
import random

quotes = {
    "The art of life is to know how to enjoy a little and to endure very much":"William Hazlitt",
    "We are here to add what we can to life, not to get what we can from life":"William Osler",
    "Life comes from the earth and life returns to the earth":"Zhuangzi",
    "If you change the way you look at things, the things you look at change":"Wayne Dyer",
    "For the great doesn't happen through impulse alone, and is a succession of little things that are brought together":"Vincent Van Gogh", \
    }

all_quotes = []

for quote, author in quotes.items():
    each_quote = f"\n'{quote}' by {author.upper()}\n"

all_quotes.append(each_quote)

print("Random Quote: ")
print(random.choice(all_quotes))