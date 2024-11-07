"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: 1B
"""

jumlah_barang = int(input("Masukkan jumlah barang: "))

if (jumlah_barang < 100):
    print("Total harga barang anda: Rp.",jumlah_barang * 5000)
elif (jumlah_barang > 150):
    (print("Total harga barang anda: Rp.",jumlah_barang * 2500))
elif (jumlah_barang >= 100):
    print("Total harga barang anda: Rp.",jumlah_barang * 4000)
