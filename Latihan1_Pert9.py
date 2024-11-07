"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: RPL 1B
"""

def volume_tabung (jarijari, tinggi):
    hasil = 3.14 * (jarijari ** 2) * tinggi #Rumus volume tabung dengan phi = 3,14
    print(hasil)
    return hasil

volume_tabung(4, 9) #Menulis jari-jari dan tinggi yang akan dihitung sesuai dengan jumlah parameter
volume_tabung(3, 12)