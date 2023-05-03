class Diskon:
    def __init__(self, total_harga):
        self.total_harga = total_harga
    
    def diskon(self):
        if self.total_harga >= 50000 and self.total_harga < 100000:
            diskon = 0.05 * self.total_harga
            return diskon
        elif self.total_harga >= 100000 and self.total_harga < 250000:
            diskon = 0.1 * self.total_harga
            return diskon
        elif self.total_harga >= 250000 and self.total_harga < 500000:
            diskon = 0.2 * self.total_harga
            return diskon
        elif self.total_harga >= 500000 and self.total_harga < 1000000:
            diskon = 0.3 * self.total_harga
            return diskon
        elif self.total_harga >= 1000000:
            diskon = 0.4 * self.total_harga
            return diskon
        else:
            diskon = 0
            return diskon

class Menu :
    def __init__ (self, nama, harga) :
        self.nama = nama
        self.harga = harga

class Kopi(Menu):
    def __init__ (self, nama, harga) :
        Menu.__init__(self, nama, harga)

    def pesan_kopi(self,jumlah_pesanan):
        ppn = self.harga * 0.1
        total_harga = self.harga * jumlah_pesanan + ppn
        diskon_obj = Diskon(total_harga)
        diskon = diskon_obj.diskon()
        total_harga -= diskon
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
            print("Diskon :", diskon*jumlah_pesanan)
            print("PPN :", int(kopi.harga * 0.1))
            print("--------------------------")
            print(f'Jumlah Bayar: Rp {total_harga:,.2f}')
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