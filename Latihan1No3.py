"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: RPL 1B
"""

angka1 = int(input("Masukkan angka: "))
angka2 = int(input("Masukkan angka: "))
angka3 = int(input("Masukkan angka: "))
angka4 = int(input("Masukkan angka: "))

def hitungtotal_ratarata (*angka):
    total = sum(angka)
    print(f"Total: {total}")
    ratarata = total / len(angka)
    print(f"Rata-rata= {ratarata}")
    return total, ratarata

hitungtotal_ratarata(angka1, angka2, angka3, angka4)
