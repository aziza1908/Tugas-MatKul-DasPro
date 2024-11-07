bebek_kecil = int(input("Masukkan banyak bebek kecil :"))

while bebek_kecil > 0:
    print("\n")
    print(bebek_kecil, "bebek kecil berenang")
    print("Menyusuri sungai yang deras")
    print("Induknya mencari kwek kwek kwek")
    bebek_kecil -= 1
    if bebek_kecil > 0:
        print("Hanya", bebek_kecil, "ekor yang pulang")
    else:
        print("Dan semua bebek kecil pulang, aha!") 