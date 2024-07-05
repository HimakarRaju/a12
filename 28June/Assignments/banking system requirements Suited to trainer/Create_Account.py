from account import create_account


def create_user():
    account_number = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    initial_balance = float(input("Enter Initial Balance: "))
    result = create_account(account_number, name, initial_balance)
    print(result)
