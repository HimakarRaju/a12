"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
Set Operations:
Write a function `common_elements(set1, set2)` that takes two sets and
returns a set containing the elements that are common to both sets.

    Example Input:
    ```python
    def common_elements(set1, set2):
        # Your code here
    print(common_elements({1, 2, 3}, {2, 3, 4}))  # Output: {2, 3}
    ```
"""


def common_elements(set1, set2):
    common_set = []
    # If sets are of same length
    if len(set1) == len(set2) or len(set1) > len(set2):
        for i in set1:
            for j in set2:
                if i == j:
                    common_set.append(i)

    # If sets are not of same length
    elif len(set1) < len(set2):
        for j in set1:
            for i in set2:
                if j == i:
                    common_set.append(i)

    return set(common_set)


print(common_elements({1, 2, 3}, {2, 3, 4}))  # Output: {2, 3}
print(common_elements({1, 2}, {2, 3, 4}))  # Output: {2}
print(common_elements({1, 2, 3, 4}, {2, 3, 4}))  # Output: {2, 3, 4}
