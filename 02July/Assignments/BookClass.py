"""
Name : HimakarRaju Gunda
Date : 02-07-2024
Trainer Name : Saynam

Description of program :
You are required to create a class book that encapsulates the details of a book.
The class should have the following private attributes:

__title     -> to store title of book
__author    -> to store author of book
__price     -> to store price of book

The class should provide the following methods:

A constructor to initialize the book's title, author and price

get_title() ->To return the title of the book
get_author() ->To return the author of the book
get_price() ->To return the price of the book

set_title(new_title)  -> To update the title of the book
set_author(new_author)  -> To update the author of the book
set_price(new_price)  -> To update the price of the book

Tasks:
Implement the book class as described
Create an instance of book and demonstrate the usage of all its methods
attempt to directly access the private attributes from the outside of the class and explain what happens
"""


class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def set_title(self, new_title):
        self.__title = new_title
        return f'updated title is {self.__title}'

    def set_author(self, new_author):
        self.__author = new_author
        return f'updated title is {self.__author}'

    def set_price(self, new_price):
        self.__price = new_price
        return f'updated title is {self.__price}'

    def get_book_details(self):
        return f'\nThe book {self.__title} is authored by {self.__author} and the price is Rs.{self.__price}'


book1 = Book("Python for dummies", "Stef Maruch", 1950)
print(book1.get_book_details())

book2 = Book("Python: The Complete Reference", "Martin C. Brown", 700)
print(book2.get_book_details())

book2.set_title("Head First Python")
book2.set_author("Paul Barry")
book2.set_price(1850)
print(book2.get_book_details())
