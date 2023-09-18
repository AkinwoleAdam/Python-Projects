'''
Temperature Converter

Description: Build a program that converts temperatures between Celsius and Fahrenheit.

Implement the conversion formulas and allow users to input temperatures in one unit and
view the equivalent temperature in the other.
Purpose: This project involves mathematical calculations and user input handling.

(°C * 9/5) + 32 = °F

5/9 * (F - 32) = C

'''

#To Fahrenheit
def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

#To Celsius
def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9


print("\nTHIS IS A TEMPERATURE CONVERTER\n")


while True:
    print("What conversions do you want to make?\n")
    print("Enter 'fahrenheit' to convert from fahrenheit to celsius\n")
    print("Enter 'celsius' to convert from celsius to fanrenheit\n")
    print("Enter 'quit' to quit program\n")

    choice = input("\nEnter an appropriate option from above: ")

    user_temp = float(input("\nEnter a suitable temperature: "))

    if user_input == 'quit':
        break

    elif choice in ['fahrenheit', 'celsius']:

        if user_input == 'fahrenheit':
            result = fahrenheit_to_celsius(user_temp)
            print(f"{user_temp}F coverted to celsius is {result}C\n")

        else:
            result = celsius_to_fahrenheit(user_temp)
            print(f"{user_temp}C coverted to fahrenheit is {result}F\n")
    else:
        print("Invalid entry, try again")

