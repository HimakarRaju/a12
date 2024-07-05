from account import BankAccount
from utils import save_account

def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    
    account = BankAccount(name, email, phone, password)
    save_account(account)
    print("Account created successfully!")
