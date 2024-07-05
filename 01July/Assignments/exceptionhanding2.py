"""
Name : HimakarRaju Gunda
Date : 01-07-2024
Trainer Name : Saynam

Description of program :
Write a function get_integer_input that prompts the user to enter a number.
Use exception handling to ensure that the user inputs a valid integer.
If the user enters a non-integer value,
catch the ValueError and prompt the user to try again until a valid integer is entered.
"""

def get_integer_inputs():
    try:
        number = int(input("Enter a Number : "))
    except ValueError:
        print("Enter a valid number")
        return get_integer_inputs()
    return number


num = get_integer_inputs()

print(f'the num is {num}')
