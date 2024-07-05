"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
Nested Data Structures:
Write a function `flatten_list(nested_lst)` that takes a list of lists and returns a single flattened list.

    Example Input:
    ```python
    def flatten_list(nested_lst):
        # Your code here
    print(flatten_list([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]
    ```
"""


def flatten_list(nested_lst):
    flatened = []
    for i in nested_lst:
        for j in i:
            flatened.append(j)
    return flatened


print(flatten_list([[1, 2], [3, 4], [5]]))
