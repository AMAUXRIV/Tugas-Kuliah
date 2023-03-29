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
            print("Buku", book.title, "berhasil dihapus dari keranjang.")
        except IndexError:
            print("Indeks buku tidak valid. Silakan coba lagi.")

    def total_price(self):
        return sum([book.price for book in self.books])


# Daftar buku
books = [
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
cart = ShoppingCart()

while True:
    print("\n1. Tampilkan daftar buku")
    print("2. Tambah buku ke keranjang")
    print("3. Tampilkan keranjang belanja")
    print("4. Hapus buku dari keranjang")
    print("5. Tampilkan total harga")
    print("6. Keluar")
    choice = input("Masukkan pilihan Anda (1/2/3/4/5/6): ")

    if choice == "1":
        print("Daftar buku:")
        for i, book in enumerate(books):
            print(f"{i+1} - {book.title} oleh {book.author} (Rp {book.price})")

    elif choice == "2":
        book_choice = int(input("Masukkan nomor buku yang ingin ditambahkan ke keranjang: "))
        if 1 <= book_choice <= len(books):
            book = books[book_choice-1]
            cart.add_book(book)
            print(f"Buku {book.title} berhasil ditambahkan ke keranjang.")
        else:
            print("Nomor buku tidak valid. Silakan coba lagi.")

    elif choice == "3":
        print("Keranjang belanja:")
        if len(cart.books) == 0:
            print("Keranjang belanja kosong.")
        else:
            for i, book in enumerate(cart.books):
                print(f"{i+1} - {book.title} oleh {book.author} (Rp {book.price})")

    elif choice == "4":
        try:
            index = int(input("Masukkan nomor buku yang ingin dihapus dari keranjang: ")) - 1
            cart.remove_book(index)
            print("Buku sudah terhapus")
        except ValueError:
            print("Nomor buku tidak valid. Silakan coba lagi.")

    elif choice == "5":
        print("Total harga keranjang belanja: Rp", cart.total_price())

    elif choice == "6":
        print("Terima kasih telah berbelanja!")
        break

    else:
      print("Pilihan tidak valid. Silakan coba lagi.")
