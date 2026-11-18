#import matplotlib.pyplot as plt
#
#bulan = ["Jan", "Feb", "Mar", "Apr", "Mei"]
#penjualan = [100, 120, 90, 140, 160]
#
#plt.plot(bulan, penjualan, marker='o', color='b')
#plt.title("Tren Penjualan Bulanan")
#plt.xlabel("Bulan")
#plt.ylabel("Penjualan")
#plt.grid(True)
#plt.show()

#import matplotlib.pyplot as plt
#jurusan = ["Informatika", "Sistem Informasi", "Desain", "Manajemen"]
#jumlah = [120, 90, 60, 110]
#plt.bar(jurusan, jumlah, color='orange')
#plt.title("Jumlah Mahasiswa per Jurusan")
#plt.xlabel("Jurusan")
#plt.ylabel("Jumlah Mahasiswa")
#plt.show()

#import matplotlib.pyplot as plt
#jam_belajar = [1, 2, 3, 4, 5, 6]
#nilai = [60, 65, 70, 75, 80, 90]
#plt.scatter(jam_belajar, nilai, color='green')
#plt.title("Hubungan Jam Belajar dan Nilai Ujian")
#plt.xlabel("Jam Belajar")
#plt.ylabel("Nilai")
#plt.show()

#import matplotlib.pyplot as plt
#kategori = ["Makanan", "Transportasi", "Hiburan", "Lainnya"]
#persentase = [40, 25, 20, 15]
#plt.pie(persentase, labels=kategori, autopct="%1.1f%%", startangle=90)
#plt.title("Komposisi Pengeluaran Bulanan")
#plt.show()

#import matplotlib.pyplot as plt
#import numpy as np
#nilai = [65, 70, 75, 80, 85, 90, 90, 95, 100, 70, 85, 80, 75, 60]
#plt.hist(nilai, bins=5, color='purple', edgecolor='black')
#plt.title("Distribusi Nilai Ujian")
#plt.xlabel("Rentang Nilai")
#plt.ylabel("Frekuensi")
#plt.show()

import matplotlib.pyplot as plt

kelas_a = [70, 75, 80, 85, 90, 95]
kelas_b = [65, 70, 75, 85, 90, 92]

plt.boxplot(
    [kelas_a, kelas_b],
    tick_labels=["Kelas A", "Kelas B"]
)

plt.title("Perbandingan Nilai Antar Kelas")
plt.ylabel("Nilai")
plt.show()