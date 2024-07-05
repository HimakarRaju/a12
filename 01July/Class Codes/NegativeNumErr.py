class NegativeNumberError(Exception):
    def __init__(self, num, message="Negative Numbers are not allowed"):
        self.num = num
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.num} -> {self.message}"


def check_positive(num):
    if num < 0:
        raise NegativeNumberError(num)
    else:
        print(f'{num} is valid')


try:
    number = int(input("Enter number : "))
    check_positive(number)
except NegativeNumberError as e:
    print(e)
