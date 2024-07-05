from account import check_account_details


def check_account_info():
    account_number = input("Enter Account Number: ")
    result = check_account_details(account_number)
    if isinstance(result, str):
        print(result)
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
