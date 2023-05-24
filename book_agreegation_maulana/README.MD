# SPESIFIK TUGAS
Program ini akan menggunakan konsep Aggregation dengan dua kelas utama yaitu Book (Buku) dan Bookstore (Toko Buku). <br>
Setiap objek Bookstore akan memiliki beberapa objek Book yang merupakan daftar buku yang tersedia di toko tersebut. <br>

# Class Book
- title (string): judul buku. <br>
- author (string): penulis buku. <br>
- price (float): harga buku. <br>

# Class BookStore
- name (string): nama toko buku. <br>
- books (list): daftar objek Book yang tersedia di toko. <br>
- Selain itu, kelas Bookstore  memiliki metode berikut: <br>

add_book(book): untuk menambahkan buku baru ke dalam daftar buku toko.<br>
display_books(): untuk menampilkan daftar buku yang tersedia beserta informasi detailnya, seperti judul, penulis, dan harga.<br>

# Class Perpus 
- display() untuk menampilkan menu
- prompt() inputan user untuk menambahkan buku
