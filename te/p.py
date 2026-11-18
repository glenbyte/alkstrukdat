
import pandas as pd

# Data penjualan
data = {
    "Bulan": [
        "Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
        "Jul", "Agu", "Sep", "Okt", "Nov", "Des"
    ],
    "Produk_A": [
        120, 135, 150, 160, 180, 200,
        210, 220, 230, 210, 190, 170
    ],
    "Produk_B": [
        80, 90, 110, 130, 150, 160,
        180, 190, 195, 200, 180, 160
    ],
    "Produk_C": [
        60, 70, 75, 85, 95, 120,
        130, 140, 150, 145, 130, 125
    ]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menyimpan ke file Excel
df.to_excel("penjualan.xlsx", index=False)

print("File penjualan.xlsx berhasil dibuat!")
