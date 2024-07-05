class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        return f'{self.title} by {self.author} published in {self.year}'


# instances of class / objects
book1 = Book("Maths Book", "XYZ", "1990")
book2 = Book("English Book", "ABC", "2000")

print(book1.get_description())
print(book2.get_description())
