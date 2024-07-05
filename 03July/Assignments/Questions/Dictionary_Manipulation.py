"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
Dictionary Manipulation:
Write a function `invert_dict(d)` that inverts the keys and values of a dictionary.

    Example Input:
    ```python
    def invert_dict(d):
        # Your code here
    print(invert_dict({'a': 1, 'b': 2, 'c': 3}))  # Output: {1: 'a', 2: 'b', 3: 'c'}
"""


def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        inverted_dict[value] = key
    return inverted_dict


# Test case
print(invert_dict({'a': 1, 'b': 2, 'c': 3}))  # Output: {1: 'a', 2: 'b', 3: 'c'}
