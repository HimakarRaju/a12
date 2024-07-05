"""
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f'{self.make}, {self.model}, {self.year}')


my_car = Car("Maruthi", "Brezza", 2024)
