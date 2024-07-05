"""

Name : HimakarRaju Gunda
Date : 27-06-2024
Trainer Name : Saynam

Description of program :
Write a program that takes a dictionary of student names and their grades.
Print the student with the highest grade.

Example:
students = {"Alice": 88, "Bob": 95, "Charlie": 90}
Output: Bob

"""

students = {"Alice": 88, "Bob": 95, "Charlie": 90}

top_student = max(students, key=students.get)

print(f"The student with the highest grade is: {top_student}")
