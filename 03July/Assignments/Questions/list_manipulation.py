"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
list_manipulation
Write a function `remove_duplicates(lst)` that takes a list of integers and returns a new list with all duplicates removed, preserving the original order.

    Example Input:
    ```python
    def remove_duplicates(lst):
        # Your code here
    print(remove_duplicates([1, 2, 3, 2, 1, 4, 5, 3]))  # Output: [1, 2, 3, 4, 5]
    ```
"""


def remove_duplicates(lst):
    uniq = []
    for element in lst:
        if element not in uniq:
            uniq.append(element)
        else:
            pass
    return uniq


print(remove_duplicates([1, 2, 3, 2, 1, 4, 5, 3]))
