"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: 1B
"""

# Informasi tentang siswa
student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"},
}

# Input nama siswa
nama = input("Masukkan nama siswa: ")

# Menggunakan method get() untuk mengakses nilai siswa tertentu
data_siswa = student_info.get(nama)

# Hasil
info_siswa = (f"Umur {nama} adalah {data_siswa["age"]} dan Prodi nya adalah {data_siswa["major"]}")
print(info_siswa)