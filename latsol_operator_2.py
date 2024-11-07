"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: 1B
"""

a = int(input("Masukka angka: "))
if (a > 0):
    print("Angka berikut termasuk angka positif")
    if (a % 2 == 0): #mengecek angka genap atau ganjil
        print("Angka berikut termasuk angka genap")
    else:
        print("Angka tersebut termasuk angka ganjil")
if (a < 0):
    print("Angka berikut termasuk angka negatif")
    if (a % 2 == 0): #mengecek angka genap atau ganjil
        print("Angka berikut termasuk angka genap")
    else:
        print("Angka tersebut termasuk angka ganjil")