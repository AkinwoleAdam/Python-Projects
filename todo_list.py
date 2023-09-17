'''
To-Do List:

Description: Create a simple to-do list application that allows users to add tasks, view their tasks,
Purpose: This project teaches you about data structures (lists), user input, 
and basic operations like adding and removing items from a list.

'''

task_list = []

def add_task(task):
    task_list.append(task)

def view_tasks():
    print("Your tasks are: \n")
    for task in task_list:
        print(task, "\n")

def remove_task(task):
    task_list.remove(task)

while True:

    print("\nWhat do you want to do?\n ")
    print("Options: ")
    print("Enter 'add' to Add Tasks")
    print("Enter 'remove' to Remove Tasks")
    print("Enter 'view' to view your Tasks")
    print("Enter 'quit' to end the program\n")

    user_input = input("Enter an appropriate option:  ")

    if user_input == 'quit':
        break

    elif user_input in ("add", "view", "remove"):

        if user_input == 'add':
            task = input("\nWhat task do you want to ask?:  ")
            add_task(task)
            print(f"Your task has been added succesfully!")

        elif user_input == 'remove':
            task = input("\nWhat task do you want to remove?:  ")

            if task in task_list:
                remove_task(task)
            else:
                print("Task not in list!")

        elif user_input == 'view':
            view_tasks()

    else:
        print("\nInvalid option")