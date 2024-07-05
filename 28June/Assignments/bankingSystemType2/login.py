from account import BankAccount
from logged_in_menu import logged_in_menu
from utils import accounts_file


def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    with open(accounts_file, "r") as file:
        accounts = file.readlines()

    for line in accounts:
        account_data = line.strip().split(",")
        if account_data[0] == name and account_data[3] == password:
            account = BankAccount(*account_data[:4], float(account_data[4]))
            print("Login successful!")
            logged_in_menu(account)
            return
    print("Invalid login credentials. Please try again.")
