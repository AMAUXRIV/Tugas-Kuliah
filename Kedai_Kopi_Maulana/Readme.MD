# Deskripsi
Program ini merupakan simulasi pemesanan kopi di Ananda Coffe. Program ini menggunakan konsep OOP (Object Oriented Programming) dengan bahasa pemrograman Python.

# Cara Penggunaan
✔ Jalankan program dengan mengakses file "index.py" pada terminal atau IDE Python. <br>
✔ Tampilan menu akan ditampilkan, kemudian masukkan kode menu dan jumlah pesanan.<br>
✔ Setelah memilih menu dan jumlah pesanan, program akan menampilkan informasi detail pesanan, termasuk diskon dan harga yang harus dibayar.<br>
✔ Setelah itu, program akan menanyakan apakah ingin memesan lagi atau tidak. Jika "y", maka program akan kembali ke tampilan menu dan memulai pesanan baru. Jika "n", maka program akan selesai. <br>
✔ Konsep OOP yang Digunakan <br>
✔ Inheritance (Pewarisan) pada class Kopi dan Menu <br>
✔ Encapsulation (Pembungkusan) pada method diskon() pada class Diskon <br>
✔ Polymorphism (Polimorfisme) pada method pesan_kopi() pada class Kopi <br>
# Class pada Program
💠 Diskon: class ini digunakan untuk menghitung diskon berdasarkan total harga. <br>
💠 Menu: class ini merupakan parent class dari class Kopi. <br>
💠 Kopi: class ini merupakan subclass dari class Menu yang merepresentasikan kopi.<br>
💠 AnandaKafe: class ini merupakan class utama yang digunakan untuk mengatur tampilan menu dan melakukan pemesanan kopi. <br>

Pada class Diskon, terdapat method diskon() yang dapat menerima self sebagai parameter, sehingga method ini dapat mengakses nilai atribut total_harga dari instance class Diskon. Dalam method diskon(), terdapat beberapa percabangan if untuk menentukan besaran diskon berdasarkan total harga. Kemudian, nilai diskon yang diperoleh dihitung dan dikembalikan sebagai output dari method diskon().
<br>
Pada class Kopi, terdapat method pesan_kopi() yang menerima self dan jumlah_pesanan sebagai parameter. Dalam method ini, terdapat beberapa perhitungan seperti perhitungan PPN dan total harga yang dihitung berdasarkan harga dan jumlah pesanan, serta penggunaan class Diskon untuk menghitung besaran diskon berdasarkan total harga. Kemudian, nilai diskon dan total harga dikembalikan sebagai output dari method pesan_kopi().
<br>
Pada class AnandaKafe, terdapat beberapa atribut dan method untuk mengelola menu dan pesanan kopi. Method pesan() digunakan untuk meminta input dari pengguna dan menjalankan perhitungan diskon dan harga total menggunakan method pesan_kopi() dari instance class Kopi. Method run() digunakan untuk menjalankan program secara keseluruhan dengan menampilkan menu dan meminta input dari pengguna menggunakan method pesan().
