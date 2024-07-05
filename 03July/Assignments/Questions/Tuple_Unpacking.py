"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
Tuple Unpacking
Write a function `swap_elements(tup)` that takes a tuple of two elements and returns a new tuple with the elements swapped.

    Example Input:
    ```python
    def swap_elements(tup):
        # Your code here
    print(swap_elements((1, 2)))  # Output: (2, 1)
"""


def swap_elements(tup):
    return tup[::-1]


print(swap_elements((1, 2)))  # Output: (2, 1)
