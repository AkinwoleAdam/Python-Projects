'''
Build a multiple-choice quiz game with a predefined set of questions and answers. 
Keep track of the user's score, display correct answers at the end, and offer a summary of their performance.
'''

quiz = {
    "Question 1: What is the capital of France?": {
        "choices": ["Paris", "Berlin", "Madrid", "Rome"],
        "correct_answer": "Paris"
    },
    "Question 2: Which planet is known as the 'Red Planet'?": {
        "choices": ["Venus", "Earth", "Mars", "Jupiter"],
        "correct_answer": "Mars"
    },
    "Question 3: Who wrote the play 'Romeo and Juliet'?": {
        "choices": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
        "correct_answer": "William Shakespeare"
    },
    "Question 4: What is the chemical symbol for gold?": {
        "choices": ["Ag", "Ge", "Au", "Hg"],
        "correct_answer": "Au"
    },
    "Question 5: Which country is known as the Land of the Rising Sun?": {
        "choices": ["China", "India", "Japan", "South Korea"],
        "correct_answer": "Japan"
    }
}

question_index = 0
score = 0
num_questions = len(quiz)

print("Welcome To My Multiple Choice Questions!\n")
print(f"You have {len(quiz)} questions to solve, get ready!\n")
print("Enter a, b, c, d depending on your answer.\n")

while question_index < num_questions:
    question = list(quiz.keys())[question_index]
    choices = quiz[question]["choices"]
    correct_answer = quiz[question]["correct_answer"]

    print(question, "\n")

    for index, answer in enumerate(choices):
        
        print(f"{chr(97 + index)}) {answer}")

    user_answer = input("Enter your answer (a, b, c, d): ").lower()
    user_choice_index = ord(user_answer) - ord('a')
    correct_answer_index = choices.index(correct_answer)

    if user_choice_index == correct_answer_index:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect answer. The correct answer is:", correct_answer, "\n")

    question_index += 1

print("You have come to the end of the game!\n")

if 1 < score <= 3:
    print(f"Your score is {score}/{len(quiz)}, you can do better,lol")
else:
    print(f"Your score is {score}/{len(quiz)}, Excellent!")