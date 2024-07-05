accounts_file = "accounts.txt"


def update_account(account):
    with open(accounts_file, "r") as file:
        accounts = file.readlines()

    with open(accounts_file, "w") as file:
        for line in accounts:
            account_data = line.strip().split(",")
            if account_data[0] == account.name:
                file.write(
                    f"{account.name},{account.email},{account.phone},{account.password},{account.balance}\n")
            else:
                file.write(line)
