"""

Name : HimakarRaju Gunda
Date : 02-07-2024
Trainer Name : Saynam

Description of program :

You are required to create a base class Appliance and a derived class WashingMachine
that demonstrates both encapsulation and inheritance. The classes should have the following
attributes and methods:

Appliance class:
Private attributes:
_brand - to store the brand of the appliance.
_ power - to store the power consumption of the appliance.

Methods:
A constructor to initialize the appliance's brand and power.
get_brand() - to return the appliance's brand.
get_power() - to return the appliance's power.

set_brand(new_brand) - to update the appliance's brand.
set_power(new_power) - to update the appliance's power.

WashingMachine class (inherits from Appliance):
Private attributes:
__capacity - to store the capacity of the washing machine in kilograms.
__mode - to store the current mode of the washing machine.

Methods:
A constructor to initialize the washing machine's brand, power, capacity, and mode.
get_capacity() - to return the capacity of the washing machine.
get_mode() - to return the current mode of the washing machine.

set_capacity(new_capacity) - to update the capacity of the washing machine.
set_mode(new_mode) - to update the mode of the washing machine.

Tasks:
Implement the Appliance and WashingMachine classes as described.
Create an instance of WashingMachine and demonstrate the usage of all its methods.
Attempt to directly access the private attributes from outside the class and explain what happens.
"""


class Appliance:  # Created class with name Appliance
    def __init__(self, brand, power):
        self.__brand = brand
        self.__power = power

    def get_brand(self):
        return self.__brand

    def get_power(self):
        return self.__power

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def set_power(self, new_power):
        self.__power = new_power


class WashingMachine(Appliance):  # Created class with name WashingMachine
    def __init__(self, capacity, mode, brand, power):
        super().__init__(brand, power)
        self.__capacity = capacity
        self.__mode = mode

    def get_capacity(self):
        return self.__capacity

    def get_mode(self):
        return self.__mode

    def set_capacity(self, new_capacity):
        self.__capacity = new_capacity

    def set_mode(self, new_mode):
        self.__mode = new_mode


# Initializing details of appliance1 using init method
appliance1 = Appliance("LG", 1000)
print(appliance1.get_brand())
print(appliance1.get_power())

appliance1.set_brand("IFB")
appliance1.set_power(2000)
print(appliance1.get_brand())
print(appliance1.get_power())

# Initializing details of machine1 using init method
machine1 = WashingMachine(10, "Normal")
print(machine1.get_capacity())
print(machine1.get_mode())

machine1.set_capacity(15)
machine1.set_mode("Performance")
print(machine1.get_capacity())
print(machine1.get_mode())
