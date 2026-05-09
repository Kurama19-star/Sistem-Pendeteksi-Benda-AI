# 🔍 Sistem Pendeteksi Benda Dalam Gambar – Kecerdasan Buatan

> **Proyek Pengembangan AI | Penglihatan Komputer | Berbasis Algoritma YOLOv8**

![Versi](https://img.shields.io/badge/Versi-1.0-blue.svg)
![Status](https://img.shields.io/badge/Status-Selesai%20%26%20Siap%20Pakai-brightgreen.svg)

---

## 📌 TENTANG PROYEK
Proyek ini merupakan sistem kecerdasan buatan yang saya kembangkan untuk mengenali, menandai, dan menghitung benda-benda yang terdapat di dalam sebuah gambar atau foto. Teknologi ini adalah dasar utama dari sistem keamanan cerdas, kendaraan otonom, analisis video, pemilahan barang industri, hingga sistem analisis olahraga.

Sistem ini dibangun menggunakan metode **YOLO (You Only Look Once) Versi 8**, yaitu algoritma pendeteksian benda paling cepat, akurat, dan paling banyak dipakai di dunia industri saat ini. Sistem mampu mengenali **80 jenis benda umum** (manusia, kendaraan, hewan, barang rumah tangga, peralatan elektronik, dll) dalam hitungan detik.

---

## 🛠️ TEKNOLOGI & ALAT YANG DIGUNAKAN
- **Bahasa Pemrograman:** Python 3.9+
- **Kerangka Kerja AI:** PyTorch, Ultralytics (YOLOv8)
- **Pengolahan Gambar:** OpenCV, Pillow
- **Tampilan Aplikasi:** Streamlit → *Bisa dijalankan lewat peramban web, mudah dipakai*

---

## ✨ FITUR UTAMA
✅ Mendeteksi dan menandai benda dengan kotak pembatas
✅ Menampilkan nama benda beserta tingkat keakuratan (%)
✅ Menghitung jumlah setiap jenis benda yang ditemukan
✅ Tampilan antarmuka sederhana, mudah dipakai siapa saja
✅ Proses sangat cepat, cocok untuk pemakaian waktu nyata

---

## 🚀 CARA MEMASANG & MENJALANKAN
1. Pasang semua kebutuhan:
```bash
pip install -r requirements.txt

---
### 📥 CARA MENGUNDUH & MEMBUKA PROYEK INI DI KOMPUTER
1. Buka halaman ini: https://github.com/Kurama19-star/Sistem-Pendeteksi-Benda-AI
2. Klik tombol hijau bertuliskan **<> Code** → pilih **Download ZIP**
3. Simpan berkas, lalu **Ekstrak / Keluarkan** semua isinya ke satu folder
4. Buka CMD / Terminal, masuk ke dalam folder tersebut
5. Pasang alat: `pip install -r requirements.txt`
6. Jalankan aplikasi: `python -m streamlit run deteksi_benda.py`

✅ Atau kalau sudah terpasang Git, ketik langsung:
`git clone https://github.com/Kurama19-star/Sistem-Pendeteksi-Benda-AI.git`