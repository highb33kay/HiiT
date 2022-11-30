class Library:
    def __init__(self, Book, Shelve):
        self.Book = Book
        self.Shelve = Shelve

    # class method
    def number_of_books(self):
        print(
            f'the number of books are: {self.Book} on Shelve Number {self.Shelve}')


class User(Library):
    def __init__(self, Book, Shelve):
        Library.__init__(self, Book, Shelve)

    def number_of_books(self):
        print("hello")


Jesse = User(41, 5)
James = Library(50, 45)

print(Jesse.number_of_books())
print(James.number_of_books())
