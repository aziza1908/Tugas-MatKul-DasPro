"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: 1B
"""

# Daftar pasangan (latitude, longitude) sebuah lokasi
Jakarta = (-6.2088, 106.8456)
Bandung = (-6.9175, 107.6191)
Surabaya = (-7.2575, 112.7521)

#a. Menampilkan data koordinat kota Bandung
koordinat_bandung = Bandung
print(f"Koordinat untuk kota Bandung adalah {koordinat_bandung}")

#b. Menampilkan jumlah lokasi yang tersimpan
Lokasi = {
    "Jakarta" : (-6.2088, 106.8456),
    "Bandung" : (-6.9175, 107.6191),
    "Surabaya" : (-7.2575, 112.7521)
}
Jumlah_Lokasi = len(Lokasi)
print(f"Jumlah lokasi yang tersimpan adalah {Jumlah_Lokasi}")
