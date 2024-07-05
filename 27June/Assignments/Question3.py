"""

Name : HimakarRaju Gunda
Date : 27-06-2024
Trainer Name : Saynam

Description of program :
Write a program that takes a list of integers and an integer as input from the user.
Check if the integer is present in the list.
If it is, print the index of its first occurrence.
If it is not, print a message saying the integer is not in the list.
"""

mylist = input("Enter the numbers with comma separating numbers and press enter : ")
mylist = mylist.split(",")
mylist = [int(x) for x in mylist]

myNum = int(input("Enter number you want to check : "))

if myNum in mylist:
    print(f'{myNum} is in the list')
else:
    print(f'{myNum} is not in the list')
