from account import add_money


def add_amount():
    account_number = input("Enter Account Number: ")
    amount = input("Enter Amount to Add: ")

    try:
        amount = float(amount)
        if amount.is_integer():
            result = add_money(account_number, float(amount))
            print(result)
        else:
            print("Amount must be a number. Please try again.")
            add_amount()
    except ValueError:
        print("Invalid input. Amount must be a number. Please try again.")
        add_amount()
