import os

accounts_file = "accounts.txt"

def save_account(account):
    with open(accounts_file, "a") as file:
        file.write(f"{account.name},{account.email},{account.phone},{account.password},{account.balance}\n")

def initialize_file():
    if not os.path.exists(accounts_file):
        open(accounts_file, "w").close()



def update_account(account):
    with open(accounts_file, "r") as file:
        accounts = file.readlines()

    with open(accounts_file, "w") as file:
        for line in accounts:
            account_data = line.strip().split(",")
            if account_data[0] == account.name:
                file.write(f"{account.name},{account.email},{account.phone},{account.password},{account.balance}\n")
            else:
                file.write(line)