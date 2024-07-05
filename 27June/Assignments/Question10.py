"""

Name : HimakarRaju Gunda
Date : 27-06-2024
Trainer Name : Saynam

Description of program :
Write a program that takes a list of integers and returns a new list
where each element is the square of the corresponding element in the original list.
Use a list comprehension for this task
.Example:Input: [1, 2, 3, 4, 5]
Output: [1, 4, 9, 16, 25]
"""

# Prompt the user to enter numbers separated by commas
input_string = input("Enter a list of integers separated by commas: ")

input_list = [int(x) for x in input_string.split(",")]  # Convert the input string to a list of integers

squared_numbers = [num ** 2 for num in input_list]

print(squared_numbers)
