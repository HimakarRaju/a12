"""

Name : HimakarRaju Gunda
Date : 27-06-2024
Trainer Name : Saynam

Description of program :
Write a program that prints all the numbers from 1 to 100. For multiples of three,
print "Fizz" instead of the number, and for the multiples of five, print "Buzz".
For numbers that are multiples of both three and five, print "FizzBuzz".
"""
for i in range(1, 101):
    print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
