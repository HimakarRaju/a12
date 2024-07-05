from abc import ABC, abstractmethod


class CookingAppliance(ABC):
    @abstractmethod
    def cook(self):
        pass


class Microwave(CookingAppliance):
    def cook(self):
        return "Cooking with microwave"


class Oven(CookingAppliance):
    def cook(self):
        return "Cooking with oven"


def start_cooking(appliance):
    print(appliance.cook())


microwave = Microwave()
oven = Oven()
start_cooking(microwave)
start_cooking(oven)
