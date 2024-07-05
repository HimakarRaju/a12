"""
Name : HimakarRaju Gunda
Date : 01-07-2024
Trainer Name : Saynam

Description of program :
Write a function divide_numbers that takes two arguments, a and b, and returns the result of dividing a by b.
Use exception handling to manage the following cases:

If b is zero, raise a ZeroDivisionError and handle it by returning a message "Cannot divide by zero."
If a or b is not a number, raise a ValueError and handle it by returning a message "Both inputs must be numbers."
"""


def div_func(a, b):
    try:
        a = int(a)
        b = int(b)
        res = a / b
    except ValueError:
        print("Both inputs must be numbers.")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None
    return res


# function call
result = div_func(2, 1)
print(result)

result2 = div_func(0, 2)
print(result2)

result3 = div_func("a", 2)
print(result3)

