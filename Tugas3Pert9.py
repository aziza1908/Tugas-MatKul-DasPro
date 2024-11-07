"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: RPL 1B
"""

jamMulai = int(input("Jam mulai: "))
menitMulai = int(input("Menit mulai: "))
detikMulai = int(input("Detik mulai: "))
    
jamSelesai = int(input("Jam selesai: "))
menitSelesai = int(input("Menit selesai: "))
detikSelesai = int(input("Detik selesai: "))

def hitungselisih(jamMulai, menitMulai, detikMulai, jamSelesai, menitSelesai, detikSelesai):
    selisihJam = jamMulai - jamSelesai
    selisihMenit = menitMulai - menitSelesai
    selisihDetik = detikMulai - detikSelesai
    print(f"Jam {selisihJam} - Menit {selisihMenit} - Detik {selisihDetik}")
    return selisihJam, selisihMenit, selisihDetik

hitungselisih(jamMulai, menitMulai, detikMulai, jamSelesai, menitSelesai, detikSelesai)