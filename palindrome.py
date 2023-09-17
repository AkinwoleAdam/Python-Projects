'''Palindrome Checker:
 Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards).'''



print("This a palindrome checker\n")

user_input = input("Enter a word: ")

reversed_word = user_input[::-1]


if reversed_word != user_input:
    print(f"\n{user_input} is not a palindrome")

else:
    print(f"\n{user_input} is a palindrome")