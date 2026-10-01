import streamlit as st
import pandas as pd

# --- Title ---
st.title("Pengeluaran Anak Kos")


# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
uang_bulanan = st.number_input("Masukkan jumlah uang bulanan Anda:", min_value=0, step=100000, format="%d")


# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
makanan = st.number_input("makanan", min_value=0, step=10000, format="%d")  # Ada 5
kos = st.number_input("kos", min_value=0, step=10000, format="%d") # Kategori
transportasi = st.number_input("transportasi", min_value=0, step=10000, format="%d") # Pengeluaran
internet = st.number_input("internet", min_value=0, step=10000, format="%d") # Pengeluaran
hiburan = st.number_input("hiburan", min_value=0, step=10000, format="%d") # Pengeluaran

# --- Tombol Ngitung Pengeluaran ---
if st.button("Hitung Pengeluaran"): # if jangan dihapus, cuman nambahin tombol disini :

    # --- Ngitung Total Pengeluaran ---
    total_pengeluaran = makanan + kos + transportasi + internet + hiburan

    # --- Ngitung Sisa Uang ---
    sisa_uang = uang_bulanan - total_pengeluaran


    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            # Tampilin uang bulanan di sini
            label="Uang Bulanan",
            value=uang_bulanan
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            label="Total Pengeluaran",
            value=total_pengeluaran
        )
    with kolom3:
        st.metric(
            # Tampilin sisa uang di sini
            label="Sisa Uang",
            value=sisa_uang
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa_uang > 0:
        st.success("keuanganmu masih aman bulan ini!")
    
    # Kondisi 2
    elif sisa_uang == 0:
        st.warning("Uang Anda habis")
    
    # Kondisi 3
    else:
        st.error("Pengeluaranmu melebihi uang bulanan!")

    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            makanan,
            kos,
            transportasi,
            internet,
            hiburan
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    # Cari pengeluaran terbesar
    pengeluaran_terbesar = df_pengeluaran["Pengeluaran"].max()
    kategori_terbesar = df_pengeluaran.loc[df_pengeluaran["Pengeluaran"] == pengeluaran_terbesar, "Kategori"].iloc[0]

    st.subheader("Pengeluaran Terbesar")
    # Tampilin pengeluaran terbesar di sini
    st.write(f"Kategori: {kategori_terbesar}")
    st.write(f"Jumlah: {pengeluaran_terbesar}")

    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    # Tampilin grafik pengeluaran di sini
    st.bar_chart(df_pengeluaran.set_index("Kategori")["Pengeluaran"])