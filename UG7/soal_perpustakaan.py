import pandas as pd
import streamlit as st

# ===== Data =====
# dictionary bersarang: {kode: {"judul", "stok"}}
KATALOG_AWAL = {
    "B01": {"judul": "Algoritma Dasar", "stok": 2},
    "B02": {"judul": "Struktur Data Python", "stok": 1},
    "B03": {"judul": "Basis Data Relasional", "stok": 2},
    "B04": {"judul": "Statistika Dasar", "stok": 1},
    "B05": {"judul": "Kalkulus 1", "stok": 3},
}


def buat_katalog():
    return {kode: dict(data) for kode, data in KATALOG_AWAL.items()}


# ===== Logika =====
def pinjam_buku(katalog, pinjaman, nama, kode):
    # return pesan error (str) kalau gagal, atau None kalau berhasil
    if nama == "":
        return "Nama peminjam wajib diisi!"

    for data in pinjaman:
        if data["nama"] == nama and data["kode"] == kode:
            return "Buku ini sudah kamu pinjam!"

    if katalog[kode]["stok"] == 0:
        return "Stok buku habis!"
        
    katalog[kode]["stok"] -= 1
    pinjaman.append({"nama": nama,"kode": kode})
    
    return None  # Ditambahkan agar eksplisit mengembalikan None saat berhasil


def kembalikan_buku(katalog, pinjaman, nama, kode):
    # return pesan error (str) kalau gagal, atau None kalau berhasil
    if nama == "":
        return "Nama peminjam wajib diisi!"

    for i, data in enumerate(pinjaman):
        if data["nama"] == nama and data["kode"] == kode:
            pinjaman.pop(i)
            katalog[kode]["stok"] += 1
            return None
    return "Data peminjaman tidak ditemukan!"


def rekap_per_peminjam(pinjaman):
    # return dictionary {nama: set kode buku yang sedang dipinjam}
    rekap = {}

    for data in pinjaman:
        nama = data["nama"]
        kode = data["kode"]

        if nama not in rekap:
            rekap[nama] = set()
        rekap[nama].add(kode)
    return rekap


# ===== Tampilan =====
def form_buku():
    nama = st.text_input("Nama peminjam").strip()
    kode = st.selectbox("Pilih buku", options=list(KATALOG_AWAL.keys()), format_func=lambda k: f"{k} - {KATALOG_AWAL[k]['judul']}")

    kol1, kol2 = st.columns(2)
    pinjam = kol1.button("Pinjam")
    kembali = kol2.button("↩️Kembalikan")
    return nama, kode, pinjam, kembali

def tampilkan_katalog(katalog):
    st.table(pd.DataFrame.from_dict(katalog, orient="index"))


def tampilkan_pinjaman(pinjaman):
    if pinjaman:
        st.table(pd.DataFrame(pinjaman))
    else:
        st.info("Belum ada buku yang sedang dipinjam.")


def tampilkan_rekap(rekap):
    if rekap:
        baris = [(nama, ", ".join(sorted(kode)), len(kode)) for nama, kode in sorted(rekap.items())]
        st.table(pd.DataFrame(baris, columns=["Nama", "Buku", "Jumlah"]).set_index("Nama"))
    else:
        st.info("Belum ada peminjam.")


# ===== Aplikasi =====
st.title("📚 Peminjaman Buku Perpustakaan")

if "katalog" not in st.session_state:
    st.session_state["katalog"] = buat_katalog()
    st.session_state["pinjaman"] = []
katalog = st.session_state["katalog"]
pinjaman = st.session_state["pinjaman"]

nama, kode, pinjam, kembali = form_buku()

if pinjam:
    pesan = pinjam_buku(katalog, pinjaman, nama, kode)

    if pesan:
        st.error(pesan)
    else:
        judul = katalog[kode]["judul"]
        st.success(f"{nama} berhasil meminjam {judul} ✅")

if kembali:
    pesan = kembalikan_buku(katalog, pinjaman, nama, kode)

    if pesan:
        st.error(pesan)
    else:
        judul = katalog[kode]["judul"]
        st.success(f"{nama} berhasil mengembalikan {judul} ✅")


st.subheader("📦 Stok Buku")
tampilkan_katalog(katalog)

st.subheader("📋 Sedang Dipinjam")
tampilkan_pinjaman(pinjaman)

st.subheader("👤 Rekap Per Peminjam")
tampilkan_rekap(rekap_per_peminjam(pinjaman))