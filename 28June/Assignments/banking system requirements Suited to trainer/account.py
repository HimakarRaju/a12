accounts = {}


def load_accounts():
    try:
        with open('accounts.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                account_number, name, balance = line.strip().split(',')
                accounts[account_number] = {
                    "name": name,
                    "balance": float(balance)
                }
        print(f'loaded data from file : \n{accounts}')
    except FileNotFoundError:
        print("File Not Found")


def save_accounts():
    with open('accounts.txt', 'w') as file:
        for account_number, details in accounts.items():
            file.write(f"{account_number},{details['name']},{details['balance']}\n")
            print(accounts)


def create_account(account_number, name, initial_balance=0):
    if account_number in accounts:
        return "Account already exists."
    accounts[account_number] = {
        "name": name,
        "balance": initial_balance
    }
    save_accounts()
    return "Account created successfully."


def add_money(account_number, amount):
    if account_number not in accounts:
        return "Account does not exist."
    accounts[account_number]["balance"] += amount
    save_accounts()
    return "Money added successfully."


def check_balance(account_number):
    if account_number not in accounts:
        return "Account does not exist."
    return accounts[account_number]["balance"]


def withdraw_money(account_number, amount):
    if account_number not in accounts:
        return "Account does not exist."
    if accounts[account_number]["balance"] < amount:
        return "Insufficient funds."
    accounts[account_number]["balance"] -= amount
    save_accounts()
    return "Money withdrawn successfully."


def check_account_details(account_number):
    if account_number not in accounts:
        return "Account does not exist."
    return {
        "account_number": account_number,
        "name": accounts[account_number]["name"],
        "balance": accounts[account_number]["balance"]
    }


# Load accounts from file when the script starts
load_accounts()
