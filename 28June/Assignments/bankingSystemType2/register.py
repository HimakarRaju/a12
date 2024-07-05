from bank_account import BankAccount

accounts_file = "accounts.txt"


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


def save_account(account):
    with open(accounts_file, "a") as file:
        file.write(
            f"{account.name},{account.email},{account.phone},{account.password},{account.balance}\n")
