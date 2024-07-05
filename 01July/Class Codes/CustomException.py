class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be between 18 to 30"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.age} -> {self.message}"


def check_age(age):
    if age < 18 or age > 30:
        raise InvalidAgeError(age)
    else:
        print(f'{age} is valid')


try:
    age_input = int(input("Enter age : "))
    check_age(age_input)
except InvalidAgeError as e:
    print(e)
