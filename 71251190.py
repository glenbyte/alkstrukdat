from bs4 import BeautifulSoup
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import requests

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

st.set_page_config(page_title="Dashboard Katalog Buku", layout="wide")
st.title("Dashboard Katalog Buku")
st.write("Mengambil data buku melalui web scraping dan kurs GBP/IDR melalui REST API.")

jumlah_halaman = st.slider("Jumlah halaman katalog yang diambil", 1, 3, 2)


if st.button("Ambil Data dan Tampilkan Dashboard", type="primary"):
    with st.spinner("Ambil Kurs GBP/IDR dan melakukan scraping data buku..."):

        res_kurs = requests.get(
            "https://api.frankfurter.dev/v2/rate/gbp/idr", timeout=10
        )
        res_kurs.raise_for_status()
        data = res_kurs.json()
        kurs_idr = float(data["rate"])

        daftar_buku = []
        for halaman in range(1, jumlah_halaman + 1):
            url = f"https://books.toscrape.com/catalogue/page-{halaman}.html"
            res = requests.get(url, timeout=10)
            res.raise_for_status()
            res.encoding = "utf-8"

            soup = BeautifulSoup(res.text, "html.parser")
            items = soup.find_all("article", class_="product_pod")
            
            for item in items:
                judul = item.h3.a["title"]
                judul_text = item.find("p",class_="price_color").get_text(strip=True)
                harga_gbp = float(judul_text.replace("£", "").strip())
                rating_teks = item.find("p", class_="star-rating")["class"][1]
                rating = RATING_MAP.get(rating_teks, 0)
                ketersediaan = item.find("p", class_="instock availability").text.strip()

                daftar_buku.append(
                {
                    "judul": judul,
                    "harga_gbp": harga_gbp,
                    "rating": rating,
                    "ketersediaan": ketersediaan,
                }
        )
        df = pd.DataFrame(daftar_buku)
        df["harga_idr"] = (df["harga_gbp"] * kurs_idr).round(2)

    st.subheader("Data Katalog Buku")
    st.caption("f{len(df)} buku diambil dari {jumlah_halaman} halaman.")
    st.dataframe(df, use_container_width=True)

    st.subheader("Visualisasi")
    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(6, 4.5))
        ax1.hist(df["harga_idr"], bins=10, edgecolor="black")
        ax1.set_title("Distribution Harga Buku")
        ax1.set_xlabel("Harga (Rupiah)")
        ax1.set_ylabel("Jumlah Buku")       
        ax1.grid(axis="y", linestyle="-", alpha=0.3)

        st.pyplot(fig1)       
    with col2:
        hitung_rating = df["rating"].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)
        fig2, ax2 = plt.subplots(figsize=(6, 4.5))
        ax2.bar(hitung_rating.index, hitung_rating.values)
        # ax2.set_xsticks([1, 2, 3, 4, 5,])    
        ax2.set_title("Jumlah Buku Berdasarkan Rating")
        ax2.set_xlabel("Rating")    
        ax2.set_ylabel("Jumlah Buku")
        ax2.grid(axis="y", linestyle="-", alpha=0.3)    
        ax2.set_axisbelow(True)    
        st.pyplot(fig2)