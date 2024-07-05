"""
Name : HimakarRaju Gunda
Date : 02-07-2024
Trainer Name : Saynam

Description of program :
Consider a program that models different geometric shapes using object-oriented programming concepts.

Implement an abstract base class Shape with two abstract methods area() and perimeter(),
which must be overridden by its subclasses Rectangle and Circle.

Write Python code to achieve this structure and demonstrate abstraction by creating instances of each
subclass (Rectangle, Circle) and calling their area() and perimeter() methods.
Instructions:

Define an abstract class Shape using the abc module.
Implement two abstract methods area() and perimeter() in the Shape class.
Create subclasses Rectangle and Circle that inherit from Shape.
Implement the area() and perimeter() methods in each subclass to return the area and perimeter of the
shape.
Instantiate one object of each subclass (Rectangle, Circle) with appropriate dimensions.
Demonstrate abstraction by calling the area() and perimeter() methods on each instance and observe the
output.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


# Create instances of Rectangle and Circle with appropriate dimensions
rectangle = Rectangle(4, 5)
circle = Circle(3)

# Demonstrate abstraction by calling the area() and perimeter() methods
print("Rectangle:")
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")

print("\nCircle:")
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")
