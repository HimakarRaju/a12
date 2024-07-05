from account import withdraw_money


def withdraw_amount():
    account_number = input("Enter Account Number: ")
    amount = input("Enter Amount to Withdraw: ")

    try:
        amount = float(amount)
        if amount.is_integer():
            result = withdraw_money(account_number, int(amount))
            print(result)
        else:
            print("Amount must be an integer. Please try again.")
            withdraw_amount()
    except ValueError:
        print("Invalid input. Amount must be a number. Please try again.")
        withdraw_amount()
