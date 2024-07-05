import os

accounts_file = "accounts.txt"

def save_account(account):
    with open(accounts_file, "a") as file:
        file.write(f"{account.name},{account.email},{account.phone},{account.password},{account.balance}\n")

def initialize_file():
    if not os.path.exists(accounts_file):
        open(accounts_file, "w").close()
