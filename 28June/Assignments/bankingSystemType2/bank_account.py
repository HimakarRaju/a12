class BankAccount:
    def __init__(self, name, email, phone, password, balance=0):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.balance = balance

    def check_balance(self):
        return self.balance

    def add_amount(self, amount):
        self.balance += amount
        return self.balance

    def withdraw_amount(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def account_details(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nBalance: {self.balance}"
