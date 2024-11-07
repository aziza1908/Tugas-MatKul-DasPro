"""
Nama: Aziza Putri Amelia
NIM: 2407784
Kelas: 1B
"""

# Data siswa dan prodi
students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

#Menghitung banyak siswa yang ada di prodi Computer Science
print("Prodi computer science sebanyak =", list(students.values()).count("Computer Science"))

#Menghitung banyak siswa yang ada di prodi Mathematics
print("Prodi mathematics sebanyak =", list(students.values()).count("Mathematics"))

#Menghitung banyak siswa yang ada di prodi Physics
print("Prodi physics sebanyak =", list(students.values()).count("Physics"))