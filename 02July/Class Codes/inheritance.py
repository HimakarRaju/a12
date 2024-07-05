class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return "Engine Started"

    def get_details(self):
        return f'{self.brand} {self.model} {self.year}'


class Car(Vehicle):
    def start_engine(self):
        return "Car Started"


class Bike(Vehicle):
    def start_engine(self):
        return "Bike Started"


my_car = Car("Toyota", "Fortuner", 2010)
my_bike = Bike("Yamaha", "FZ-S", 2020)

print(my_car.get_details())
print(my_car.start_engine())

print(my_bike.get_details())
print(my_bike.start_engine())
