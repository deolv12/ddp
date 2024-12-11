from Animal import *

class Burung (Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.jenis = jenis
        self.warna = warna

    def cetak_merak(self):
        super().cetak()
        print("jenis \t: ", self.jenis, 
              "\nWarna \t: ", self.warna)
    
merak = Burung("Merak", "Serangga", "Hutan Tropis", "Bertelur", "Green Peafowl", "Hijau")
merak.cetak_burung()
hantu = Burung("Hantu", "Serangga", "Hutan, pegunungan", "Bertelur", "ural owl", "Hitam")
hantu.cetak_burung()