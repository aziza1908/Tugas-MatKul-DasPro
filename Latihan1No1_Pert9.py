"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: RPL 1B
"""


def fibonacci(n): #parameter n untuk berapa panjang deret yang akan ditampilkan
    if n <= 0:
        return[]
    elif n == 1:
        return[0] 
    elif n == 2:
        return[0, 1] #ketika n == 2, akan menampilkan [0, 1] karena dua bilangan awal deret fibonacci
    else:
        deret = fibonacci(n-1)
        deret.append(deret[-1] + deret[-2]) #Rumus
        return deret

N = int(input("Masukkan jumlah bilangan yang ingin ditampilkan dalam deret fibonacci: "))
print(f"Deret fibonacci: {fibonacci(N)}")

