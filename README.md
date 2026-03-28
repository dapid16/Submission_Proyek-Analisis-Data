# 🛒 **Proyek Analisis Data — E-Commerce Public Dataset**

## 👨‍💻 **Profil Analis**

* **Nama:** Muhammad David Firdaus
* **Email:** [muhammaddavid025@gmail.com](mailto:muhammaddavid025@gmail.com)
* **ID Dicoding:** smilepid

---

## 📖 **Ringkasan Proyek**

Proyek ini merupakan *submission* akhir untuk kelas **Belajar Fundamental Analisis Data** dari Dicoding.
Analisis difokuskan pada *E-Commerce Public Dataset* untuk menjawab pertanyaan bisnis utama terkait performa penjualan, tren bulanan, serta kategori produk paling diminati.

Selain analisis dasar, proyek ini juga dilengkapi dengan **Customer Segmentation menggunakan metode RFM (Recency, Frequency, Monetary)** untuk mengidentifikasi pelanggan bernilai tinggi.
Seluruh hasil analisis divisualisasikan melalui *dashboard* interaktif berbasis Streamlit.

---

## 📌 **Tujuan dan Ruang Lingkup**

Proyek ini mencakup proses analisis data secara end-to-end, yaitu:

1. **Data Wrangling**

   * Mengumpulkan data
   * Menilai kualitas dan struktur data (*assessing*)
   * Membersihkan data (*cleaning*), termasuk:

     * Menangani *missing values*
     * Mengonversi tipe data
     * Menghapus *outlier* menggunakan metode **Interquartile Range (IQR)**

2. **Exploratory Data Analysis (EDA)**

   * Menggali pola transaksi
   * Menganalisis tren penjualan
   * Menemukan kategori produk dengan performa terbaik

3. **Data Visualization**

   * Menjawab pertanyaan bisnis menggunakan visualisasi berupa **Bar Chart**, **Line Chart**, dan grafik pendukung lainnya.

4. **RFM Customer Segmentation**

   * Menghitung skor RFM
   * Mengelompokkan pelanggan berdasarkan nilai bisnisnya
   * Mengidentifikasi kelompok pelanggan prioritas seperti **VIP customers**

5. **Interactive Dashboard**

   * Membangun *dashboard* dengan Streamlit untuk menampilkan:

     * Tren penjualan
     * Produk terlaris
     * Distribusi pelanggan berdasarkan skor RFM

---

## 📂 **Struktur Direktori**

Struktur folder dalam proyek ini dirancang agar mudah dipahami dan diakses:

```text
submission/
├── dashboard/
│   ├── dashboard.py       # Aplikasi Streamlit untuk visualisasi data
│   └── main_data.csv      # Dataset yang telah dibersihkan (post-wrangling)
├── notebook.ipynb         # Notebook yang berisi seluruh proses analisis
├── README.md              # Dokumentasi proyek
└── requirements.txt       # Daftar dependency Python
```

---
## 🚀 Cara Menjalankan Dashboard (Lokal)

Ikuti langkah-langkah di bawah ini untuk menjalankan *dashboard* di komputer lokal Anda:

**1. Clone Repositori Ini**
Buka terminal/command prompt, lalu jalankan perintah:
```bash
git clone [Submission_Proyek-Analisis-Data_Muhammad-David-Firdaus.git](https://github.com/dapid16/Submission_Proyek-Analisis-Data)
cd nama-repositori
```

**2. Buat Virtual Environment (Opsional namun disarankan)**
```bash
python -m venv env
# Untuk Windows:
env\Scripts\activate
# Untuk Mac/Linux:
source env/bin/activate
```

**3. Install Dependencies**
Pastikan Anda berada di direktori yang terdapat file `requirements.txt`, lalu jalankan:
```bash
pip install -r requirements.txt
```

**4. Masuk ke Folder Dashboard dan Jalankan Aplikasi Streamlit**
Karena *file* aplikasi dan dataset berada di dalam *folder* `dashboard`, Anda harus masuk ke *folder* tersebut terlebih dahulu sebelum menjalankannya:
```bash
cd dashboard
streamlit run dashboard.py
```
Aplikasi akan secara otomatis terbuka di *browser default* Anda melalui `http://localhost:8501`.
