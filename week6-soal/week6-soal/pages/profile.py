import streamlit as st
from user import user_data_by_username

# CEK APAKAH SUDAH LOGIN
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.switch_page("app.py")

username = st.session_state.username    
user = user_data_by_username()
user_data = user[username]
# hint untuk mematikan text input ada di -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# BUAT 2 INPUT TEXT 1 Username 1 Password namun disable/matikan field Username dan yang password harus tipe password
st.title("profile")
username = st.text_input("username", value=username, disabled=True)
password = st.text_input("password", value=user_data["password"], type="password")
# Silahkan kalau mau baca baca ini hehe ga wajib ya-> https://discuss.streamlit.io/t/buttons-alignment/51929
col1, space, col2 = st.columns([1,3,1])
with col1:
    # Buat tombol logout st.button("logout", type="primary") keluar ke app.py
    if st.button("Logout", type="primary"):
        st.session_state.login = False
        st.rerun()

with col2:
    
    # Ini untuk ubah password st.button("Ganti Data", type="secondary", width=400)
    # Kondisi -> Password baru dan lama ga boleh sama 
    # Jika sama -> st.error("ga boleh sama wok")
    # jika beda ubah melalui variabel 'user' lalu tampilkan st.success("Berhasil")
    if st.button("ganti data", type="secondary", width=400):
        if password == user[st.session_state.username]["password"]:
            st.error("ga boleh sama wok")
        else:
            user[st.session_state.username]["password"] = password
            st.success("Berhasil")