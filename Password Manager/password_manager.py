def view():
    with open("Password Manager/passwords.txt",'r') as f:
        for index, line in enumerate(f.readlines()):
            print(f"Account{index + 1}: {line.rstrip()}")

def add():
    account = input("\nEnter account name:  ")
    password = input("\nEnter account password:  ")

    with open("Password Manager/passwords.txt",'a') as f:
        f.write(f'Account Name:{account}, Password: {password}\n')


# master_password is user's name 
master_password = input("Enter master password to access your passwords: ")

while True:
    print("\nWhat do you want to do?\n ")
    print("Options: ")
    print("Enter 'add' to Add an account password")
    print("Enter 'view' to view your account passwords ")
    print("Enter 'quit' to end the program\n")

    user_input = input("Enter an appropriate option:  ")

    if user_input == 'quit':
        break

    elif user_input in ("add", "view"):
        if user_input == 'add':
            add()
            print(f"\nYour account has been added succesfully!")
        else:
            view()
    else:
        print("Invalid entry, check and try again.")
