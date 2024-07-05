"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
Function and Exception Handling:
Write a function `safe_divide(a, b)` that takes two numbers and returns their division result.
If division by zero is attempted, catch the exception and return `None`.

    Example Input:
    ```python
    def safe_divide(a, b):
        # Your code here
    print(safe_divide(10, 2))  # Output: 5.0
    print(safe_divide(10, 0))  # Output: None
    ```
"""


def safe_divide(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        return None


print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: None
