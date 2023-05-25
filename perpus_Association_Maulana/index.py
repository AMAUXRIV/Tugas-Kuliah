class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.retrn_book = []

    def borrow_book(self, book):
        print ("_________________________________________")
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} has borrowed {book.title} by {book.author}")
        else:
            print(f"{book.title} by {book.author} is not available for borrowing")

    def return_book(self, book):
        print ("_________________________________________")
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            self.retrn_book.append(book)
            print(f"{self.name} has returned {book.title} by {book.author}")
        else:
            print(f"{self.name} did not borrow {book.title} by {book.author}")

    def display_borrowed_books(self):
        print ("_________________________________________")
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"{book.title} by {book.author} (available: {book.is_available})")
            print (f"{self.name} has return the following books:")
            for book in self.retrn_book :
                print (f"{book.title} by {book.author} (available: {book.is_available})")
            
        else:
            print(f"{self.name} has not borrowed any books yet")

member = LibraryMember("John")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

member.borrow_book(book1)
member.borrow_book(book2)
member.display_borrowed_books()

member.return_book(book1)
member.display_borrowed_books()