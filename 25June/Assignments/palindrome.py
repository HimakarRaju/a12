#
"""
Name : HimakarRaju Gunda
Date : 25-06-2024
Trainer Name : Saynam

Description of program :
Write a Python program that takes a string input from the user and checks if it is a palindrome.
A palindrome is a string that reads the same backward as forward

Program to check if a string is a palindrome
"""


# # Method1
# string = input("Enter a string\n")          # Get user input
# if string == string[::-1]:                  # Check if the string is a palindrome
#     print("The string is a palindrome\n")
# else:
#     print("The string is not a palindrome\n")


# # Method2
# String = input("Enter a string\n")
# inverse_string = reversed(String)
# if list(String) == list(inverse_string):
#     print("The string is a palindrome\n")
# else:
#     print("The string is not a palindrome\n")


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True  # 0 is a palindrome
    else:
        str_x = str(x)
        return str_x == str_x[::-1]


# Test cases
print(is_palindrome(121))  # Output: True
print(is_palindrome(300))  # Output: False
