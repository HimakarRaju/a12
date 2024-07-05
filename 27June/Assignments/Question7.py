"""

Name : HimakarRaju Gunda
Date : 27-06-2024
Trainer Name : Saynam

Description of program :
Write a program that takes a string as input from the user
and counts the number of vowels (a, e, i, o, u) in the string.

Example:

Input: hello world
Output: 3

"""
# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Define the vowels
vowels = "aeiouAEIOU"

# Initialize the count of vowels
vowel_count = 0

# Iterate through each character in the string and count the vowels
for char in user_input:
    if char in vowels:
        vowel_count += 1

# Print the result
print(f"Number of vowels: {vowel_count}")
