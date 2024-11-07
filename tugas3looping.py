"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: RPL 1B
"""

#Titik awal
x = 1

#Lopping bekerja jika x kurang dari atau sama dengan 50
while x <= 50:
    if x % 5 == 0: #Untuk memastikan apabila x merupakan kelipatan 5
        print("pass") #Apabila x merupakan kelipatan 5 maka outputnya "pass"
        x += 1 #Untuk melanjutkan ke angka yang selanjutnya
        continue #Supaya lompat ke iterasi yang selanjutnya
    print(x) #Apabila x bukan kelipatan maka print nilai x
    x += 1 #Untuk melanjutkan ke angka yang selanjutnya