"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: RPL 1B
"""

def hitungtotal_ratarata(angka):
    total = sum(angka)                 
    ratarata = total / len(angka)      
    return total, ratarata

angka = []  

while True:
    input_angka = (input("Masukkan angka (ketik 'hitung' untuk memulai menghitung): "))
    
    if input_angka.lower() == 'hitung':
        break  
    angka.append(int(input_angka))
    
if angka:
    total, ratarata = hitungtotal_ratarata(angka)
    print(f"Total: {total}")
    print(f"Rata-rata= {ratarata}")
else:
    print("Tidak dapat menghitung")