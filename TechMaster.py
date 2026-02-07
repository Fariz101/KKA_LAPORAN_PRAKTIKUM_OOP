from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        self.__stok = stok 
        self.__harga_dasar = harga_dasar  

    def get_harga_dasar(self):
        return self.__harga_dasar
    
    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")
        else:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")

class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor
        self.pajak_pembelian = 0.10

    def tampilkan_detail(self):
       print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
       print(f" Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(10%): Rp {self.get_harga_dasar() * self.pajak_pembelian:,.0f}".replace(',', '.'))

    def hitung_harga_total(self, jumlah):
        harga_plus_pajak = self.get_harga_dasar() * (1 + self.pajak_pembelian)
        return harga_plus_pajak * jumlah

class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, camera):
        super().__init__(nama, stok, harga_dasar)
        self.camera = camera
        self.pajak_pembelian = 0.05 

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.camera}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(5%): Rp {self.get_harga_dasar() * self.pajak_pembelian:,.0f}".replace(',', '.'))

    def hitung_harga_total(self, jumlah):
        harga_plus_pajak = self.get_harga_dasar() * (1 + self.pajak_pembelian)
        return harga_plus_pajak * jumlah

def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---", end="")
    total_tagihan = 0
    nomor = 1
    
    for i, jumlah in daftar_barang:
        print(f"\n{nomor}. ", end="")
        i.tampilkan_detail() 
        subtotal = i.hitung_harga_total(jumlah)
        print(f"Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}".replace(',', '.'))
        total_tagihan += subtotal
        nomor += 1

    print("\n----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}".replace(',', '.'))
    print("----------------------------------------")


print("Plaintext")
print("--- SETUP DATA ---")
laptop1 = Laptop("ROG Zephyrus", 0, 20000000, "Ryzen 9")
smartphone1 = Smartphone("iPhone 13", 0, 15000000, "12MP")

laptop1.tambah_stok(10)
smartphone1.tambah_stok(-5)
smartphone1.tambah_stok(20)

keranjang = [
    (laptop1, 2),
    (smartphone1, 1)
]

proses_transaksi(keranjang)