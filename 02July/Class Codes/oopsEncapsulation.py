class BackAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return f'The balance is Rs.{self.__balance}'


account = BackAccount("Himakar", 1000)

account.deposit(500)
account.withdraw(200)
print(account.get_balance())
