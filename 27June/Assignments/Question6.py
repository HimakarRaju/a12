"""

Name : HimakarRaju Gunda
Date : 27-06-2024
Trainer Name : Saynam

Description of program :
Write a program that reads a file called "input.txt" and
prints its contents line by line.
If the file does not exist, print a message saying the file could not be found.
"""

import os

# Check if the file exists
if os.path.isfile("input.txt"):
    # Open and read the file
    with open("input.txt", "r") as file:
        # Print each line in the file
        for line in file:
            # 'end' parameter is used to avoid adding extra newlines
            print(line, end='')
        file.close()
else:
    # Print a message if the file is not found
    print("The file 'input.txt' could not be found.")
