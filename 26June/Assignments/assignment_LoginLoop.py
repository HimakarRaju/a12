"""

Name : HimakarRaju Gunda
Date : 26-06-2024
Trainer Name : Saynam

Description of program :
Write a Python program that prompts the user to enter a password. I
f the password entered is "Python123", print "Access granted."
If the password is incorrect, print "Incorrect password, try again."
Continue prompting the user for a password until the correct password is entered.
"""


def login():
    password = input("Enter your password: ")
    if password == "Python123":
        print("Access Granted\n")
    else:
        print("Incorrect password try again\n")
        login()


login()
