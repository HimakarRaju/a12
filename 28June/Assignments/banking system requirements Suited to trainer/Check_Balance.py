from account import check_balance


def check_amount():
    account_number = input("Enter Account Number: ")
    result = check_balance(account_number)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Balance for account number {account_number}: {result}")
