"""

Name : HimakarRaju Gunda
Date : 02-07-2024
Trainer Name : Saynam

Description of program :
Write a program that takes a list of dictionaries
(each dictionary representing a student with "name" and "grades" keys)
and prints the average grade of each student.
"""
# Example list of dictionaries representing students
students = [
    {"name": "Alice", "grades": [88, 92, 95]},
    {"name": "Bob", "grades": [72, 85, 91]},
    {"name": "Charlie", "grades": [90, 89, 94]}
]

# Calculate and print the average grade for each student
for student in students:
    name = student["name"]
    grades = student["grades"]

    # Calculate the average grade
    if len(grades) > 0:
        average_grade = sum(grades) / len(grades)
    else:
        average_grade = 0  # Handle case where there are no grades

    print(f"{name}: Average grade = {average_grade}")
