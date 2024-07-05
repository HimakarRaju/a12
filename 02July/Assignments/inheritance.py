"""

Name : HimakarRaju Gunda
Date : 02-07-2024
Trainer Name : Saynam

Description of program :
You are required to create a base class person and a derived class employee
that demonstrates the concept of inheritance.
The classes should have the following attributes and methods:

person class:
private attributes :

__name -> to store person's name
--age  -> to store person's age

methods:

A constructor to initialize the persons name and age.
get_name() -> to return the person's name
get_age()  -> to return the person's age

set_name(new_name)  -> to update the person's name
set_age(new_age)    -> to update the person's age

Employee class (inherits from person)

private attributes:
__employee_id -> to store employee's ID.
__salary      -> to store employee's salary

methods:

A constructor to initialize the employees name,age,salary

get_employee_id() -> to return the employee's ID
get_salary()      -> to return the employee's salary

set_employee_id(new_employee_id) -> to update the employee's ID
set_salary(new_salary)           -> to update the employee's salary

Tasks:

Implement the person and employee class as described
create an instance of employee and demonstrate the usage of all its methods.
attempt to directly access the private attributes form outside the class
and explain what happens.
"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


class Employee(Person):
    def __init__(self, employee_id, salary, name, age):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def set_employee_id(self, new_employee_id):
        self.__employee_id = new_employee_id

    def set_salary(self, new_salary):
        self.__salary = new_salary


# Initializing details of person1 using init method
person1 = Person("Rakesh", 24)
# getting details of person1 using get methods
print(person1.get_name())
print(person1.get_age())

# Updating details of person1 using set methods
person1.set_name("Bhargav")
person1.set_age(25)
# confirming update using get methods
print(person1.get_name())
print(person1.get_age())

# Initializing details of emp1 using init method
emp1 = Employee(1, 25000)
# getting details of emp1 using get methods
print(emp1.get_employee_id())
print(emp1.get_salary())

# Updating details of person1 using set methods
emp1.set_employee_id('001')
emp1.set_salary(30000)
# confirming update using get methods
print(emp1.get_employee_id())
print(emp1.get_salary())
