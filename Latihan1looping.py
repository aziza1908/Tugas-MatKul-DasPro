login = 3
print("Silahkan Login")
while login > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == "loginUTS" and password == rpl2024:
        print("Selamat datang di aplikasi Prodi RPL")
        break
    else:
        login-=1
        if login > 0:
            print(f"Login salah! Kesempatan Anda {login} x lagi.")
        else:
            print("Anda tidak diperkenankan mengakses aplikasi ini.")
