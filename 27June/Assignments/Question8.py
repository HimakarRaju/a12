"""

Name : HimakarRaju Gunda
Date : 27-06-2024
Trainer Name : Saynam

Description of program :
Write a program that takes a list of integers and
returns a new list containing only the even numbers from the original list.
Use a list comprehension for this task.

Example:

Input: [1, 2, 3, 4, 5, 6]
Output: [2, 4, 6]

"""
# Solution
# Prompt the user to enter numbers separated by spaces
input_string = input("Enter a list of integers separated by spaces: ")

# Convert the input string to a list of integers
input_list = [int(x) for x in input_string.split()]

# Use a list comprehension to create a new list with only the even numbers
even_numbers = [num for num in input_list if num % 2 == 0]

# Print the result
print(f"Even numbers: {even_numbers}")
