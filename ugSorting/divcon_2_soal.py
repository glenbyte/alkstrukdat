# Data mahasiswa dan 5 nilai UG
mahasiswa = [
    {"nama": "Andi", "nilai": [80, 75, 90, 70, 85]},
    {"nama": "Budi", "nilai": [60, 65, 70, 55, 60]},
    {"nama": "Citra", "nilai": [90, 85, 95, 88, 92]},
    {"nama": "Deni", "nilai": [70, 75, 65, 72, 68]},
    {"nama": "Eka", "nilai": [85, 80, 78, 90, 87]},
    {"nama": "Fajar", "nilai": [65, 70, 68, 60, 72]},
    {"nama": "Gina", "nilai": [88, 92, 85, 90, 87]},
    {"nama": "Hadi", "nilai": [75, 80, 70, 78, 72]},
    {"nama": "Intan", "nilai": [55, 60, 65, 58, 62]},
    {"nama": "Joko", "nilai": [78, 82, 75, 80, 85]}
]


# Menghitung rata-rata nilai setiap mahasiswa
for mhs in mahasiswa:
    mhs["rata_rata"] = sum(mhs["nilai"]) / len(mhs["nilai"])


# Divide and Conquer - Merge Sort
def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    kiri = merge_sort(data[:mid])
    kanan = merge_sort(data[mid:])

    kiri = merge_sort(kiri)
    kanan = merge_sort(kanan)

    return merge(kiri, kanan)


def merge(kiri, kanan):
    result = []
    i = 0
    j = 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i]["rata_rata"] >= kanan[j]["rata_rata"]:
            result.append(kiri[i])
            i += 1
        else:
            result.append(kanan[j])
            j += 1
    result.extend(kiri[i:])
    result.extend(kanan[j:])
    return result
# Menghitung rata-rata keseluruhan
rata_rata_keseluruhan = sum(mhs["rata_rata"] for mhs in mahasiswa) / len(mahasiswa) if mahasiswa else 0

# Mengurutkan mahasiswa menggunakan Merge Sort
mahasiswa_urut = merge_sort(mahasiswa)

atas = []
bawah = []
for mhs in mahasiswa_urut:
    if mhs["rata_rata"] >= rata_rata_keseluruhan:
        atas.append(mhs)
    else:
        bawah.append(mhs)
# Menampilkan hasil rata-rata keseluruhan

print(f"\nRata-rata Keseluruhan: {rata_rata_keseluruhan}")

print("\n=== DI ATAS / SAMA DENGAN RATA-RATA ===")

# Tampilkan List di atas / sama dengan rata-rata
for mhs in mahasiswa_urut:
    if mhs["rata_rata"] >= rata_rata_keseluruhan:
        print(f"{mhs['nama']}: {mhs['nilai']}: {mhs['rata_rata']}")

print("\n=== DI BAWAH RATA-RATA ===")

# Tampilkan List di bawah rata-rata
for mhs in mahasiswa_urut:
    if mhs["rata_rata"] < rata_rata_keseluruhan:
        print(f"{mhs['nama']}: {mhs['nilai']}: {mhs['rata_rata']}")