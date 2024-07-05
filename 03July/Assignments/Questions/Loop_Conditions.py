"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
 Loop and Condition:
Write a function `fizz_buzz(n)` that prints the numbers from 1 to n. But for multiples of three print "Fizz"
instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

    Example Input:
    ```python
    def fizz_buzz(n):
        # Your code here
    fizz_buzz(15)
    # Output:
    # 1
    # 2
    # Fizz
    # 4
    # Buzz
    # Fizz
    # 7
    # 8
    # Fizz
    # Buzz
    # 11
    # Fizz
    # 13
    # 14
    # FizzBuzz
    ```
"""


def fizz_buzz(n):
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print(fizz_buzz(15))
