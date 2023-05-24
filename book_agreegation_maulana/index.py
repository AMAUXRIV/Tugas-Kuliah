class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class BookStore:
    def __init__(self, name, books=None):
        self.name = name
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title}\nAuthor: {book.author}\nPrice: {book.price}\n----------------")

class Perpus:
    def __init__(self):
        self.bookstore = BookStore("My Bookstore")

    def display(self):
        print("""
        1. Tampilkan Buku
        2. Tambah Buku
        """)

    def prompt(self):
        title = input("Book Title: ")
        author = input("Book Author: ")
        price = float(input("Book Price: "))
        book = Book(title, author, price)
        self.bookstore.add_book(book)

my_perpus = Perpus()

while True:
    my_perpus.display()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        my_perpus.bookstore.display_books()
    elif choice == 2:
        my_perpus.prompt()
    else:
        break