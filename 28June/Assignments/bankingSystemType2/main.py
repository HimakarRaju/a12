import os
from register import register
from login import login
from utils import initialize_file


def main():
    initialize_file()

    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Thanks for visiting us.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
