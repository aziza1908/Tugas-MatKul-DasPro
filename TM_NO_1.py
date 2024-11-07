"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: 1B
"""

# Daftar nilai 10 Mahasiswa
Nilai_Mahasiswa = [88, 75, 63, 97, 82, 74,91, 80, 81, 63]

#Soal a
#Nilai Maksimum
print("Daftar nilai mahasiswa: ", Nilai_Mahasiswa)
print("Nilai maksimum dari data tersebut adalah ", max(Nilai_Mahasiswa))

#Nilai Minimum
print("Daftar nilai mahasiswa: ", Nilai_Mahasiswa)
print("Nilai minimum dari data tersebut adalah ", min(Nilai_Mahasiswa))

#Nilai rata-rata
print("Daftar nilai mahasiswa: ", Nilai_Mahasiswa)
total = sum(Nilai_Mahasiswa)/len(Nilai_Mahasiswa)
print("Rata - rata dari data tersebut adalah ", total)

#Soal b
def angka_terbesar_kedua(x) :
    terbesar = max(x)
    x.remove(terbesar)
    return max(x)
Nila_Mahasiswa = [88, 75, 63, 97, 82, 74,91, 80, 81, 63]
terbesar_kedua = angka_terbesar_kedua(Nilai_Mahasiswa)
print("Daftar nilai mahasiswa: ", Nilai_Mahasiswa)
print("Angka terbesar kedua dari data tersebut adalah ", terbesar_kedua)