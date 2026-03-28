import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="E-Commerce Public Dataset Dashboard", page_icon="🛒", layout="wide")

sns.set_theme(style='darkgrid')

def create_monthly_orders_df(df):
    df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)
    monthly_orders = df.groupby('order_month')['order_id'].nunique().reset_index()
    return monthly_orders

def create_category_orders_df(df):
    category_orders = df.groupby('product_category_name_english')['order_id'].count().reset_index()
    category_orders = category_orders.rename(columns={'order_id': 'order_count'})
    category_orders_sorted = category_orders.sort_values(by='order_count', ascending=False)
    return category_orders_sorted

def create_rfm_df(df):
    recent_date = df['order_purchase_timestamp'].max() + pd.Timedelta(days=1)
    rfm_df = df.groupby('customer_id').agg({
        'order_purchase_timestamp': lambda x: (recent_date - x.max()).days,
        'order_id': 'nunique',
        'price': 'sum'
    }).reset_index()
    rfm_df.columns = ['customer_id', 'Recency', 'Frequency', 'Monetary']
    return rfm_df

@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

all_df = load_data()

# ==========================================
# FITUR INTERAKTIF: FILTER TANGGAL (SIDEBAR)
# ==========================================
min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_purchase_timestamp"].max()

with st.sidebar:
    st.title("👨‍💻 Profil Analis")
    st.markdown("""
    **Proyek Analisis Data:** E-commerce Public Dataset  
    **Nama:** Muhammad David Firdaus  
    **Email:** muhammaddavid025@gmail.com  
    **ID Dicoding:** smilepid
    """)
    st.divider()
    
    # Mengambil start_date & end_date dari date_input
    st.header("📅 Filter Rentang Waktu")
    try:
        start_date, end_date = st.date_input(
            label='Pilih Tanggal',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
    except ValueError:
        st.error("Pilih rentang waktu yang valid!")
        st.stop()

# ==========================================
# MENERAPKAN FILTER PADA DATAFRAME UTAMA
# ==========================================
main_df = all_df[(all_df["order_purchase_timestamp"] >= str(start_date)) & 
                 (all_df["order_purchase_timestamp"] <= str(end_date))]

# Memanggil helper function menggunakan data yang SUDAH DIFILTER (main_df)
monthly_orders_df = create_monthly_orders_df(main_df)
category_orders_df = create_category_orders_df(main_df)
rfm_df = create_rfm_df(main_df)

# ==========================================
# KOMPONEN UI STREAMLIT
# ==========================================
st.title('🛒 E-Commerce Public Dataset Dashboard')
st.markdown("""
Selamat datang di **E-Commerce Public Dataset Dashboard**! 📊  
Aplikasi ini menyajikan hasil analisis data fundamental dari *E-commerce Public Dataset*. 
Gunakan **filter rentang waktu** di *sidebar* untuk melihat perubahan data metrik dan visualisasi secara dinamis.
""")

st.divider()

st.subheader("📌 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pesanan", value=main_df['order_id'].nunique())
with col2:
    st.metric("Total Pendapatan", value=f"R$ {main_df['price'].sum():,.2f}")
with col3:
    st.metric("Total Pelanggan Unik", value=main_df['customer_id'].nunique())

st.divider()

st.subheader('📈 Tren Pesanan Bulanan')
fig, ax = plt.subplots(figsize=(16, 8))
sns.lineplot(
    x='order_month', 
    y='order_id', 
    data=monthly_orders_df, 
    marker='o', 
    linewidth=2, 
    color="#72BCD4",
    ax=ax
)
ax.set_title("Dinamika Jumlah Pesanan per Bulan", loc="center", fontsize=20, pad=20)
ax.set_xlabel("Bulan", fontsize=12)
ax.set_ylabel("Total Pesanan", fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig)

with st.expander("💡 Klik untuk melihat Insight Tren Penjualan"):
    st.write("""
    **Penjelasan & Insight:** Grafik garis di atas memvisualisasikan jumlah pesanan unik per bulan. Terlihat bahwa jumlah pesanan mengalami fluktuasi yang dinamis. Ada periode di mana pesanan naik signifikan, kemungkinan besar didorong oleh kampanye promosi musiman, hari libur, atau *event* diskon. Sebaliknya, ada pula bulan-bulan dengan tren menurun. Perusahaan perlu menganalisis lebih dalam *event* apa yang terjadi pada bulan puncak tersebut untuk mereplikasi kesuksesannya di masa mendatang.
    """)

st.divider()

st.subheader('📦 Pola Penjualan Kategori Produk')
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

top_5 = category_orders_df.head(5)
bottom_5 = category_orders_df.tail(5)

sns.barplot(x="order_count", y="product_category_name_english", data=top_5, palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Jumlah Terjual", fontsize=12)
ax[0].set_title("Top 5 Kategori Paling Laris", loc="center", fontsize=18, pad=15)

sns.barplot(x="order_count", y="product_category_name_english", data=bottom_5, palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Jumlah Terjual", fontsize=12)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Bottom 5 Kategori Paling Sepi", loc="center", fontsize=18, pad=15)
st.pyplot(fig)

with st.expander("💡 Klik untuk melihat Insight Kategori Produk"):
    st.write("""
    **Penjelasan & Insight:** Berdasarkan rentang waktu yang dipilih, bar chart di sebelah kiri menyoroti dominasi kategori **`bed_bath_table`** (peralatan kamar tidur dan mandi) sebagai produk yang paling banyak terjual. Di sisi kanan, kita bisa melihat kategori **`computers`** merupakan yang paling sepi peminat. Keputusan bisnis yang bisa diambil dari data ini adalah memperkuat inventaris dan kampanye iklan pada produk unggulan (Top 5), sembari melakukan evaluasi strategi harga atau *clearance sale* untuk produk-produk di Bottom 5.
    """)

st.divider()

st.subheader("👑 Best Customer Based on RFM Parameters")
st.write("Menampilkan Top 5 pelanggan VIP berdasarkan total nilai transaksi (Monetary) terbesar:")

st.dataframe(
    rfm_df.sort_values(by='Monetary', ascending=False).head().style.format({"Monetary": "R$ {:.2f}"}), 
    use_container_width=True
)

with st.expander("💡 Klik untuk melihat Insight RFM Analysis"):
    st.write("""
    **Penjelasan & Insight:** Tabel ini adalah hasil segmentasi pelanggan menggunakan parameter RFM (*Recency, Frequency, Monetary*). Lima pelanggan yang ditampilkan di atas merupakan pelanggan lapis pertama (VIP) karena mereka memiliki skor **Monetary** tertinggi (menyumbang pendapatan terbesar). Langkah strategis selanjutnya adalah menjaga loyalitas mereka melalui program retensi eksklusif, seperti memberikan *voucher* khusus, akses prioritas produk baru, atau diskon *member*.
    """)

st.caption('Copyright (c) Dicoding 2026 - Muhammad David Firdaus')