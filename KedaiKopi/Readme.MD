# AnandaKafe
AnandaKafe adalah program sederhana untuk memesan kopi di Ananda Coffe. Program ini dibuat menggunakan bahasa pemrograman Python.

## ◽ Cara Penggunaan
⨀ Jalankan file anandakafe.py.
⨀ Tampilkan daftar menu dengan memilih opsi 1.
⨀ Pilih menu kopi yang ingin dipesan dengan memasukkan kode menu (A, B, C, atau D).
⨀ Masukkan jumlah pesanan.
⨀ Program akan menampilkan detail pesanan, termasuk harga, diskon, PPN, dan total harga yang harus dibayar.
⨀ Jika ingin memesan lagi, pilih opsi y. Jika tidak, pilih opsi n.
⨀ Program akan berakhir.

## ◽ Struktur Program
⨀ Program AnandaKafe terdiri dari beberapa kelas, yaitu:

🔹 Menu: kelas dasar untuk semua jenis menu.
🔹 Kopi: kelas turunan dari Menu untuk jenis menu kopi.
🔹 AnandaKafe: kelas utama yang mengelola daftar menu dan melakukan pesanan.

Program AnandaKafe berjalan dengan menggunakan method run() dari kelas AnandaKafe. Method ini akan menampilkan daftar menu dan melakukan pesanan. Setelah pesanan selesai dilakukan, program akan menanyakan apakah pengguna ingin memesan lagi atau tidak.