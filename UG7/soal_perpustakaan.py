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
    if kode in katalog:
        return f" {nama} Berhasil meminjam buku"

    for k in pinjam:
        return f"buku ini sudah kamu pinjam"  
    if kode in pinjaman :
        return f"stok buku habis"
    
    pinjaman.append({"nama" : nama, "kode": kode})
    katalog[kode]["stok"] -= 1
    return None
    
   
def kembalikan_buku(katalog, pinjaman, nama, kode):
    # return pesan error (str) kalau gagal, atau None kalau berhasil
    if nama not in pinjaman:
        return f"data peminjaman tidak ditemukan"
    if nama == "":
        return "Nama peminjam wajib diisi"

    pinjaman.remove((nama, kode))
    katalog[kode]["stok"] += 1
    return None

def rekap_per_peminjam(pinjaman):
    # return dictionary {nama: set kode buku yang sedang dipinjam}
    if pinjaman:
        rekap = {}
        for nama , kode in pinjaman:
            if nama not in rekap:
                rekap[nama] = set()
            rekap[nama].add(kode)
        return rekap

# ===== Tampilan =====
def form_buku():
    # lengkapi kode def form_buku() untuk input nama dan kode
    # return (nama peminjam, kode buku, tombol Pinjam ditekan?, tombol Kembalikan ditekan?)
    # nama dibaca APA ADANYA (case-sensitive), hanya spasi di pinggir yang dibuang

    # nama = ? (TO DO)
    # kode = ? (TO DO)
    # kol1, kol2 = st.columns(2)
    # pinjam = kol1.button("📖 Pinjam")
    # kembali = kol2.button("↩️ Kembalikan")
    # return nama, kode, pinjam, kembali
    
    nama = st.text_input("Nama peminjam").strip()
    kode = st.input("Kode buku").strip()
    kol1, kol2 = st.columns(2)
    pinjam = kol1.button("📖 Pinjam")
    kembali = kol2.button("↩️ Kembalikan")
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


# B. kerjakan di sini:
#    - kalau `pinjam`  -> panggil pinjam_buku(...)
#    - kalau `kembali` -> panggil kembalikan_buku(...)
#    keduanya: kalau ada pesan -> st.error(pesan), kalau tidak -> st.success("... berhasil ...")

if pinjam:
    pesan = pinjam_buku(katalog, pinjaman, nama, kode)
    if pesan:
        st.error(pesan)
    else:
        judul = katalog[kode]["judul"]
        st.success
if kembali:
    pesan = kembalikan_buku(katalog, pinjaman, nama, kode)
    if pesan:
        st.error(pesan)
    else:
        st.success(f"Buku '{kode}' berhasil dikembalikan oleh '{nama}'.")
st.subheader("📦 Stok Buku")
tampilkan_katalog(katalog)

st.subheader("📋 Sedang Dipinjam")
tampilkan_pinjaman(pinjaman)

st.subheader("👤 Rekap Per Peminjam")
tampilkan_rekap(rekap_per_peminjam(pinjaman))