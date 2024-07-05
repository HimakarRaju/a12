"""
Name : HimakarRaju Gunda
Date : 01-07-2024
Trainer Name : Saynam

Description of program :
Write a function read_file that takes a filename as argument
and returns the content of the file.
Use exception handling to manage the following cases

If the file does not exist, catch the FileNotFoundError and return
a message "File not Found."

If there is an error reading the file, Catch the IOError and return
a message "Error Reading File"
"""


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return f'The file contents are :\n{content}'
    except FileNotFoundError:
        print("File Not Found")
    except IOError:
        print("Error Reading File")


file_contents = read_file("file1.txt")
print(file_contents)

