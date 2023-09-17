'''Word Counter: Develop a program that counts the number of words, characters, and sentences in a text input.'''

print("This is WORD COUNTER!")
print("I will count the number of words, characters and sentences in your input")

def counter(text):

    #word_counter
    word_counter = len(text.split())

    #characters counter
    character_counter = len(text)

    #sentences_counter
    sentences_counter = len(text.split("."))

    return word_counter, character_counter, sentences_counter


text = input("Enter a word, characters or sentences to count:  ")

word_counter, character_counter, sentence_counter = counter(text)

# Display results
print(f"Word Count: {word_counter}")
print(f"Character Count: {character_counter}")
print(f"Sentence Count: {sentence_counter}")