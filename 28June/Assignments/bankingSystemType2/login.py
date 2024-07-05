from bank_account import BankAccount
from update_account import update_account, accounts_file


def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    with open(accounts_file, "r") as file:
        accounts = file.readlines()

    for line in accounts:
        account_data = line.strip().split(",")
        if account_data[0] == name and account_data[3] == password:
            account = BankAccount(*account_data[:4], float(account_data[4]))
            print("Login successful!")
            logged_in_menu(account)
            return
    print("Invalid login credentials. Please try again.")


def logged_in_menu(account):
    while True:
        print("\n1. Check Balance")
        print("2. Add Amount")
        print("3. Withdraw Amount")
        print("4. Account Details")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your balance is: {account.check_balance()}")
        elif choice == "2":
            amount = float(input("Enter amount to add: "))
            account.add_amount(amount)
            print(
                f"Amount added successfully! New balance: {account.check_balance()}")
            update_account(account)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            result = account.withdraw_amount(amount)
            if result == "Insufficient funds":
                print(result)
            else:
                print(
                    f"Amount withdrawn successfully! New balance: {account.check_balance()}")
                update_account(account)
        elif choice == "4":
            print(account.account_details())
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
