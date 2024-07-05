"""
Name : HimakarRaju Gunda
Date : 02-07-2024
Trainer Name : Saynam

Description of program :
Consider a program that models different types of vehicles using object-oriented programming concepts.

Implement a base class Vehicle with a method move() that is overridden by its subclasses Car, Boat, and Plane.

Each subclass should implement the move() method to display a message specific to its type of vehicle.

Write Python code to achieve this structure and demonstrate polymorphism by creating instances of each
subclass (Car, Boat, Plane) and calling their move() methods.

Instructions:
Define a class Vehicle with an _init_ method to initialize a name attribute.
Implement a method move() in the Vehicle class which prints a generic message (e.g., "Vehicle is moving").

Create subclasses Car, Boat, and Plane inheriting from Vehicle.
Override the move() method in each subclass to print a message specific to the type of vehicle (e.g., "Car is
driving on the road").

Instantiate one object of each subclass (Car, Boat, Plane).
Demonstrate polymorphism by calling the move() method on each instance and observe the specific
messages printed.
"""


class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def move(self):
        return f"{self.name} Car is driving on the road"


class Boat(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def move(self):
        return f"{self.name} Boat is Moving on the water"


class Plane(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def move(self):
        return f"{self.name} Plane is flying in the sky"


car = Car("Chevrolet")
print(car.move())

boat = Boat("Cruize")
print(boat.move())

plane = Plane("Boeing")
print(plane.move())
