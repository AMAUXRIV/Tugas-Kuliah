class Menu :
    def __init__ (self, nama, harga) :
        self.nama = nama
        self.harga = harga
class Kopi(Menu):
    def __init__ (self, nama, harga) :
        Menu.__init__(self, nama, harga)

    def pesan_kopi(self,jumlah_pesanan):
        ppn = self.harga * 0.1
        if jumlah_pesanan > 5 :
            diskon = self.harga * 0.2
            total_harga = self.harga * jumlah_pesanan - diskon + ppn
        else :
            diskon = 0
            total_harga = self.harga * jumlah_pesanan + ppn
        return  diskon, total_harga
class AnandaKafe :
    def __init__(self):
        self.daftar_kopi = [
            Kopi("ES Kopi Susu", 11000),
            Kopi("ES Kopi Coklat", 12000),
            Kopi("ES Kopi Hitam", 11000),
            Kopi("Ice Americano", 14000)
        ]
        self.daftar_menu = {
            "a" : self.daftar_kopi[0],
            "b" : self.daftar_kopi[1],
            "c" : self.daftar_kopi[2],
            "d" : self.daftar_kopi[3]
        }

    def tampilkan_menu(self):
        print("""
        ==============================
        
        Ananda Coffe
        List Menu Minuman Kopi
     
        ==============================
        A. ES Kopi Susu : Rp 11.000
        B. ES Kopi Coklat : Rp 12.000
        C. ES Kopi Hitam : Rp 11.000
        D. Ice Americano : Rp 14.000
        ==============================
        """)

    def pesan(self):
        pesan = input("Masukkan Kode Menu : ").lower()
        jumlah_pesanan = int(input("Masukkan Jumlah Pesanan : "))

        if pesan in self.daftar_menu :
            kopi = self.daftar_menu[pesan]
            diskon, total_harga = kopi.pesan_kopi(jumlah_pesanan)

            print("--------------------------")
            print("Ananda Coffe")
            print("--------------------------")
            print("Menu :", kopi.nama)
            print("Jumlah Pesan :", jumlah_pesanan)
            print("Harga :", kopi.harga)
            print("Diskon :", diskon)
            print("PPN :", int(kopi.harga * 0.1))
            print("--------------------------")
            print("Jumlah Bayar : Rp {:,.0f}".format(total_harga))
            print("--------------------------")
        else:
            print("Menu tidak tersedia.")
            self.pesan()

    def run(self):
        self.tampilkan_menu()
        self.pesan() 
        pilihan = input("Apakah anda ingin memesan lagi? (y/n) : ")
        if pilihan.lower() == "y" :
            self.run()
        else :
            print("Terima kasih telah berkunjung ke Ananda Coffe")

cafe = AnandaKafe()
cafe.run()