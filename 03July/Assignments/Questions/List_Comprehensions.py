"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
Write a function `square_even_numbers(lst)` that takes a list of integers and
returns a list of squares of the even numbers using list comprehensions.

    Example Input:
    ```python
    def square_even_numbers(lst):
        # Your code here
    print(square_even_numbers([1, 2, 3, 4, 5]))  # Output: [4, 16]
    ```
"""


def square_even_numbers(lst):
    squared_even_numbers = [i ** 2 for i in lst if i % 2 == 0]
    return squared_even_numbers


print(square_even_numbers([1, 2, 3, 4, 5]))
