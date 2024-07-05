"""
Name : HimakarRaju Gunda
Date : 27-06-2024
Trainer Name : Saynam

Description of program :
Write a program that takes a list of tuples representing student names and their grades,
and prints a set of students who scored more than 75.

Example:

students = [("Alice", 88), ("Bob", 72), ("Charlie", 90)]
Output: {'Alice', 'Charlie'}

"""

# Example list of tuples with student names and their grades
students = [("Alice", 88), ("Bob", 72), ("Charlie", 90)]

# Create a set of students who scored more than 75
top_students = {name for name, grade in students if grade > 75}

# Print the result
print(f"Students who scored more than 75: {top_students}")
