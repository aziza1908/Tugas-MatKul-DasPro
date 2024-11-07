"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas : RPL 1B
"""

jumlah = 0

while True:
    angka = int(input("Masukkan angka: "))
    if angka < 0:
        break
    jumlah += angka

print("Total=", jumlah)
