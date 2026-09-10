# import ini jangan dihapus/diedit yak
import random


def totalPenjualan(a, b):
    # kerjakan di sini
    if b == 0:
        return 0
    return a[b - 1][1] + totalPenjualan(a, b - 1)
def penjualanTertinggi(a, b):
    # kerjakan di sini
    if b == 1:
        return a[0]
    tertinggiSebelumnya = penjualanTertinggi(a, b - 1)
    if a[b - 1][1] > tertinggiSebelumnya[1]:
        return a[b - 1]
    else:
        return tertinggiSebelumnya

def diAtasRataRata(a, b):
    # kerjakan di sini
    jumlah = 0
    for namaBarang in penjualan:
        if penjualan[namaBarang] > rataRata:
            jumlah += 1
    return jumlah

# Program Utama - Jangan dihapus/diedit yak
angka = int(input("NIM: "))
random.seed(angka)

barang = [
    "Beras",
    "Minyak",
    "Gula",
    "Telur",
    "Kopi",
    "Teh"
]

penjualan = {}

for namaBarang in barang:
    penjualan[namaBarang] = random.randint(100, 500)

data = list(penjualan.items())
n = len(data)

print("\n===== Data Penjualan =====")
for namaBarang, jumlah in penjualan.items():
    print(namaBarang, ":", jumlah)

total = totalPenjualan(data, n)
tertinggi = penjualanTertinggi(data, n)
rataRata = total / n
jumlahDiAtasRataRata = diAtasRataRata(penjualan, rataRata)

print("\n===== Hasil Analisis =====")
print("Total penjualan        :", total)
print("Penjualan tertinggi    :", tertinggi[0], "(", tertinggi[1], ")")
print("Rata-rata penjualan    :", round(rataRata, 2))
print("Di atas rata-rata      :", jumlahDiAtasRataRata, "barang")