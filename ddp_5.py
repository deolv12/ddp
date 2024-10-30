# 1. buat variabel list dengan value
kendaraan = ["vario", "motor", "160cc", "hitam", "roda 2"]
kendaraan.append ("29.000.000")
kendaraan.append ("matic")
print (kendaraan)
kendaraan.insert (2, "honda")
print (kendaraan)

# 2. buat program phyton dengan match case untuk menghitung luas bangun datar
pilihan = int(input("""Pilih nomor pilihan:  
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran 
3. Menghitung Luas Segitiga : """))
 
match pilihan :
    case 1 : 
        print("Menghitung Luas Persegi")
        s = int(input("masukan nilai sisi: "))
        luasPersegi = s * s
        print(f"Luas persegi dengan sisi {s} adalah {luasPersegi}")
    case 2 : 
        print("Menghitung Luas Lingkaran")
        pi = 3.14
        r = int(input("Masukan nilai jari jari: "))
        luasLingkaran = pi * r ** 2
        print(f"Luas Lingkaran dengan jari jari {r} adalah {luasLingkaran}")
    case 3 :
        print("Menghitung Luas Segitiga")
        alas = int(input("Masukan nilai alas: "))
        tinggi = int(input("Masukan nilai tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")
    case _ :
        print("input tidak valid")
