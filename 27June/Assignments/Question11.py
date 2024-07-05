"""
Name : HimakarRaju Gunda
Date : 02-07-2024
Trainer Name : Saynam

Description of program :
Write a program that takes a string from the user and replaces all vowels with the character '*'.
Example:Input: "hello world"
Output: "h*ll* w*rld"
"""

input_string = input("Enter a string : ")

vowels = 'aeiouAEIOU'

output = ''.join(['*' if char in vowels else char for char in input_string])

print(output)
