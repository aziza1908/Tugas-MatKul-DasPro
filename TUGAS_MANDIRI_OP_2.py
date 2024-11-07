"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: 1B
"""

#Masukkan input
gender = input("Gender anda wanita/pria: ")
umur = int(input("Masukkan umur anda: "))
tinggi_badan = int(input("Masukkan tinggi badan anda: "))
iq = int(input("Masukkan IQ anda: "))

if gender == "Wanita" and tinggi_badan >= 170 and iq >= 130 and 18<= umur <= 25:
    print("Anda dapat menjadi seorang model catwalk")
elif gender == "Pria" and tinggi_badan >= 175 and iq >= 130 and 18<= umur <= 25:
    print("Anda dapat menjadi seorang model catwalk")
else:
    print("Anda tidak dapat menjadi seorang model catwalk")