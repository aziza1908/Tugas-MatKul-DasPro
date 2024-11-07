"""
Nama: Aziza Putri Amelia
Kelas: RPL 1B
NIM: 2407784
Kelompok 9 - Zephyr
"""

#Posisi awal
#A = sisi sungai awal
#B = sisi sungai akhir

sisi_A = ["P1", "I1", "P2", "I2", "P3", "I3"]
sisi_B = []

#Langkah 1
print("Langkah 1: I1 & I2 menyebrang ke sisi B")
sisi_A.remove("I1")
sisi_A.remove("I2")
sisi_B.append("I1")
sisi_B.append("I2")
print(f"Posisi sisi A: {sisi_A}")
print(f"Posisi sisi B: {sisi_B}")
print("*" * 15)

#Langkah 2.1
print("Langkah 2.1: I2 kembali ke sisi A")
sisi_A.append("I2")
sisi_B.remove("I2")
print(f"Posisi sisi A: {sisi_A}")
print(f"Posisi sisi B: {sisi_B}")
print("*" * 15)

#Langkah 2.2
print("Langkah 2.2: I1 dan I3 menyebrang ke sisi B")
sisi_A.remove("I2")
sisi_A.remove("I3")
sisi_B.append("I2")
sisi_B.append("I3")
print(f"Posisi sisi A: {sisi_A}")
print(f"Posisi sisi B: {sisi_B}")
print("*" * 15)

#Langkah 3.1
print("Langkah 3.1: I2 kembali ke sisi A")
sisi_A.append("I2")
sisi_B.remove("I2")
print(f"Posisi sisi A: {sisi_A}")
print(f"Posisi sisi B: {sisi_B}")
print("*" * 15)

#Langkah 3.2
print("Langkah 3.2: P1 dan P3 menyebrang ke sisi B")
sisi_A.remove("P1")
sisi_A.remove("P3")
sisi_B.append("P1")
sisi_B.append("P3")
print(f"Posisi sisi A: {sisi_A}")
print(f"Posisi sisi B: {sisi_B}")
print("*" * 15)

#Langkah 4.1
print("Langkah 4.1: I1 kembali ke sisi A")
sisi_A.append("I1")
sisi_B.remove("I1")
print(f"Posisi sisi A: {sisi_A}")
print(f"Posisi sisi B: {sisi_B}")
print("*" * 15)

#Langkah 4.2
print("Langkah 4.2: P2 dan I2 menyebrang ke sisi B")
sisi_A.remove("P2")
sisi_A.remove("I2")
sisi_B.append("P2")
sisi_B.append("I2")
print(f"Posisi sisi A: {sisi_A}")
print(f"Posisi sisi B: {sisi_B}")
print("*" * 15)

#Langkah 5
print("Langkah 5: I1 menyebrang sendiri ke sisi B")
sisi_A.remove("I1")
sisi_B.append("I1")
print(f"Posisi sisi A: {sisi_A}")
print(f"Posisi sisi B: {sisi_B}")
print("*" * 15)

print("Semua pasangan berhasil menyebrang sungai")