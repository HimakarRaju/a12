from Add_Money import add_amount
from Check_Account_info import check_account_info
from Check_Balance import check_amount
from Create_Account import create_user
from Withdraw_Amount import withdraw_amount


def main():
    active = True
    while active:
        print(
            "\n1. Create Account\n2. Check Balance\n3. Add Amount\n4. Withdraw Amount\n"
            "5. Check Account Details\n6.Exit\n")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            check_amount()
        elif choice == "3":
            add_amount()
        elif choice == "4":
            withdraw_amount()
        elif choice == "5":
            check_account_info()
        elif choice == "6":
            active = False
            print("Exiting the system.")
        else:
            print("Invalid choice. Please try again.")


main()
