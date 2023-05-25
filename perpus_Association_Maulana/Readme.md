# Program 
Menggunakan konsep Association antara dua kelas utama yaitu Book (Buku) dan LibraryMember (Anggota Perpustakaan).<br>
Setiap objek LibraryMember akan terkait dengan beberapa objek Book yang merupakan daftar buku yang dipinjam oleh anggota tersebut. Berikut adalah spesifikasinya: <br>

# Class Book dengan atribut berikut:

title (string): judul buku. <br>
author (string): penulis buku.<br>
is_available (bool): status ketersediaan buku (True jika tersedia, False jika sedang dipinjam).<br>

Class LibraryMember dengan atribut berikut:<br>

name (string): nama anggota perpustakaan. <br>
borrowed_books (list): daftar objek Book yang dipinjam oleh anggota.<br>

Selain itu, kelas LibraryMember harus memiliki metode berikut:<br>

borrow_book(book): untuk meminjam buku dengan menambahkannya ke dalam daftar buku yang dipinjam oleh anggota.<br>
return_book(book): untuk mengembalikan buku dengan menghapusnya dari daftar buku yang dipinjam oleh anggota.<br>
display_borrowed_books(): untuk menampilkan daftar buku yang dipinjam oleh anggota beserta informasi detailnya, seperti judul, penulis, dan status ketersediaan.<br>
Implementasikan kelas-kelas Book dan LibraryMember sesuai dengan spesifikasi di atas.<br>

Lakukan beberapa peminjaman dan pengembalian buku. Panggil metode display_borrowed_books() untuk menampilkan daftar buku yang dipinjam oleh anggota.
