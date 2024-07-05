"""
Name : HimakarRaju Gunda
Date : 25-06-2024
Trainer Name : Saynam

Description of program :
Write a detailed pseudocode for a simple program that takes a number as input,
calculates the square if it's even or the cube if it's odd, and then outputs the result.
Incorporate conditional and looping constructs.

**Program: Calculate Square or Cube**
"""
number = int(input("Enter a number : "))

if number % 2 == 0:
    result = number ** 2
else:
    result = number ** 3
print(result)
