class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, index):
        try:
            book = self.books.pop(index)
            print(f"Buku {book.title} berhasil dihapus dari keranjang.")
        except IndexError:
            print("Indeks buku tidak valid. Silakan coba lagi.")

    def total_price(self):
        return sum(book.price for book in self.books)


# Daftar buku
BOOKS = [
    Book("The Alchemist", "Paulo Coelho", 85.0),
    Book("The Da Vinci Code", "Dan Brown", 110.0),
    Book("To Kill a Mockingbird", "Harper Lee", 70.0),
    Book("1984", "George Orwell", 65.0),
    Book("Pride and Prejudice", "Jane Austen", 60.0),
    Book("The Catcher in the Rye", "J.D. Salinger", 75.0),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 90.0),
    Book("The Hobbit", "J.R.R. Tolkien", 95.0),
    Book("The Lord of the Rings", "J.R.R. Tolkien", 120.0),
    Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 100.0)
]

# Program Utama
def display_books():
    print("Daftar buku:")
    for i, book in enumerate(BOOKS):
        print(f"{i+1} - {book.title} oleh {book.author} (Rp {book.price})")
        """
        book.title diambil dari atribut title pada objek book yang diberikan pada metode add_book() di kelas ShoppingCart.
        Saat metode add_book() dipanggil dengan objek buku sebagai argumen, objek buku tersebut dimasukkan ke dalam daftar self.books yang didefinisikan dalam metode __init__() di kelas ShoppingCart. 
        Kemudian, saat metode display_cart() dipanggil,objek buku dari daftar self.books diproses dalam loop for yang mengambil atribut title dari objek buku dengan menggunakan sintaks book.title.
        """

def add_book_to_cart():
    book_choice = int(input("Masukkan nomor buku yang ingin ditambahkan ke keranjang: "))
    if 1 <= book_choice <= len(BOOKS):
        book = BOOKS[book_choice-1]
        cart.add_book(book)
        print(f"Buku {book.title} berhasil ditambahkan ke keranjang.")
    else:
        print("Nomor buku tidak valid. Silakan coba lagi.")

def display_cart():
    print("Keranjang belanja:")
    if len(cart.books) == 0:
        print("Keranjang belanja kosong.")
    else:
        for i, book in enumerate(cart.books):
            print(f"{i+1} - {book.title} oleh {book.author} (Rp {book.price})")

def remove_book_from_cart():
    try:
        index = int(input("Masukkan nomor buku yang ingin dihapus dari keranjang: ")) - 1
        cart.remove_book(index)
    except ValueError:
        print("Nomor buku tidak valid. Silakan coba lagi.")

def display_total_price():
    print(f"Total harga keranjang belanja: Rp {cart.total_price()}")

cart = ShoppingCart()

while True:
    print("\n1. Tampilkan daftar buku")
    print("2. Tambah buku ke keranjang")
    print("3. Tampilkan keranjang belanja")
    print("4. Hapus buku dari keranjang")
    print("5. Tampilkan total harga")
    print("6. Keluar")
    choice = input("Masukkan pilihan Anda (1/2/3/4/5/6)\n")
    if choice == "1":
      display_books()
    elif choice == "2":
      add_book_to_cart()
    elif choice == "3":
      display_cart()
    elif choice == "4":
      remove_book_from_cart()
    elif choice == "5":
      display_total_price()
    elif choice == "6":
      print("Terima kasih telah berbelanja di toko buku kami.")
      break
    else:
      print("Pilihan tidak valid. Silakan coba lagi.")

