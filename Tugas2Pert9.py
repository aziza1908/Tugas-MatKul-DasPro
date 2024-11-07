"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: RPL 1B
"""

"""Pak budi juga menambahkan bahwapassword ini harus sudah ada dalam sistem yang di buat, 
sehingga sistem ituhanya mengecek password saja tanpa memperdulikan username.
Maka hanya mengecek password saja
"""

Password = "Latihan"

def login(password, kesempatan=3):
    while kesempatan > 0:
        inputUsername = input("Masukkan Username: ")
        inputPassword = input("Masukkan Password: ")

        if inputPassword == password:
            print("Login berhasil")
            return True
        else:
            kesempatan -= 1
            print(f"Username atau password salah, silahkan coba lagi. Kesempatan anda {kesempatan}x lagi.")

            if kesempatan ==0:
                print("Anda gagal login karena telah salah memasukkan password yang salah sebanyak 3 kali.")
                return False
            
login(Password)
