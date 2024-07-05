"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
File Handling:
Write a function `count_lines(file_path)` that takes a file path as input and returns the number of lines in the file.

    Example Input:
    ```python
    def count_lines(file_path):
        # Your code here
    # Assume 'sample.txt' contains:
    # Hello World
    # Python Programming
    print(count_lines('sample.txt'))  # Output: 2
    ```
"""


def count_lines(fine_name: str):
    try:
        with open(fine_name, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return None

    return len(lines)


print(count_lines('sample.txt'))  # Output: 2
