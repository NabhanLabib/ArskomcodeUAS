import streamlit as st

st.markdown(":blue-background[**Nama : Nabhan Labib**]")
st.markdown(":blue-background[**NIM : 312310783**]")
st.markdown(":blue-background[**Kelas : TI.23.C.7**]")

st.title("**ANALISA DATA INVENTARIS GUDANG**")
st.write("Masukkan Data yang ingin anda Analisa..")

uploaded_file = st.file_uploader("Pilih dan Unggah File", type="txt")

if uploaded_file is not None:
    st.write("**Daftar Barang Tersedia:**")
    
    # Baca file dan proses data
    lines = uploaded_file.getvalue().decode("utf-8").splitlines()
    headers = lines[0].strip().split(',')
    data = []
    total_inven = 0
    max_stock = 0
    max_stock_product = ""
    max_revenue_product = ""
    max_revenue = 0
    
    for line in lines[1:]:
        items = line.strip().split(',')
        nama_barang = items[0].strip()
        jumlah = int(items[1].strip())
        harga_satuan = int(items[2].strip())

        # Menghitung total nilai per barang
        nilai_barang = jumlah * harga_satuan
        total_inven += nilai_barang
        
        # Mencari Barang dengan stok terbanyak
        if jumlah > max_stock:
            max_stock = jumlah
            max_stock_product = nama_barang
        
        # Mencari produk dengan Nilai tertinggi
        if nilai_barang > max_revenue:
            max_revenue = nilai_barang
            max_revenue_product = nama_barang
        
        # Membuat format data untuk ditampilkan
        data.append([nama_barang, jumlah, harga_satuan])

    # Tampilkan daftar produk dalam bentuk tabel
    st.table([headers]+data)
    
    # Menampilkan Total Nilai Inventaris
    st.write(f" - Total Nilai Inventaris :  ***Rp. {total_inven}***")
    
    # Menampilkan barang dengan Stok Terbanyak
    st.write(f" - Barang dengan Stok Terbanyak: ***{max_stock_product}*** (dengan stok sebanyak {max_stock} buah)")
    
    # Menampilkan Barang dengan Nilai tertinggi
    st.write(f" - Barang dengan Nilai Tertinggi: ***{max_revenue_product}*** (senilai Rp {max_revenue})")


st.markdown(
    """
    <style>
    /* Mengubah Latar Belakang baris dan kolom */
    th {
        background-color: #696969;
    /* Mengubah warna Latar Belakang bagian sel data */
    td {
        background-color: #F0FFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

