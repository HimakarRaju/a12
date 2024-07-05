"""

Name : HimakarRaju Gunda
Date : 26-06-2024
Trainer Name : Saynam

Description of program :
Write a Python program that calculates the sum of all numbers divisible by 3 or 5 below a given number n.
Prompt the user to enter a number n and then compute and print the sum of all such numbers.

eg :
Enter a number: 20
Sum of numbers divisible by 3 or 5 below 20 is 78.
"""
# Prompt the user to enter a number n
number = int(input("Enter a number: "))

total_sum = 0

for i in range(1, number):
    # Check if the number is divisible by 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        total_sum += i

# Print the sum
print(f"The sum of all numbers divisible by 3 or 5 below {number} is :  {total_sum}")
