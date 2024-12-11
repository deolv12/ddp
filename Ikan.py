from Animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, bentuk_gigi):
        super().__init__(nama, makanan, hidup, berkembang_biak) 
        self.warna = warna
        self.bentuk_gigi = bentuk_gigi

    def cetak_ikan(self):
        super().cetak()
        print("warna \t\t\t: ", self.warna, 
              "\nbentuk_gigi \t\t: ", self.bentuk_gigi)
    
salmon = Ikan("Salmon", "amphipoda", "Air tawar", "Bertelur", "abu-abu", "gading babi")
salmon.cetak_ikan()
paus = Ikan("Paus", "carnivora", "Laut", "Melahirkan", "hitam", "gigi besar")
paus.cetak_ikan()