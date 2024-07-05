"""
Name : HimakarRaju Gunda
Date : 02-07-2024
Trainer Name : Saynam

Description of program :
Create a class student initialize with name, age & class
write a function get_details() for getting details of the student

Tasks:
implement the functionality as described
create an instance showing all the functions
"""


class StudentDetails:
    def __init__(self, name, age, cls):
        self.name = name
        self.age = age
        self.cls = cls

    def get_details(self):
        return f'{self.name} of {self.age} years is from class {self.cls}'


student1 = StudentDetails("Rajesh", "19", "10")
student2 = StudentDetails("Vivek", "18", "10")

print(student1.get_details())
print(student2.get_details())
