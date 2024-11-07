angka = 0
ganjil = 0
genap = 0

while angka >= 0:
    angka = int(input("Masukkan angka: "))
    
    if angka < 0:
        break

    menentukan = angka % 2
    
    if menentukan == 0:
        genap += angka
    else:
        ganjil += angka

print(genap)
print(ganjil)