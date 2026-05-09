# ==================================================
# PROYEK : SISTEM PENDETEKSI BENDA DALAM GAMBAR
# TEKNOLOGI : PYTHON + ULTRALYTICS + YOLOv8
# VERSI : 2.0 (Ditingkatkan Akurasi & Fitur)
# DESKRIPSI : Aplikasi AI mengenali benda, akurat, lengkap, tampilan rapi
# DIBUAT OLEH : Kurniadi Wira Kusuma
# ==================================================

# === 1. IMPOR SEMUA ALAT DAN PUSTAKA ===
from ultralytics import YOLO   
import cv2                      
import streamlit as st         
from PIL import Image, ImageFont, ImageDraw
import numpy as np

# === 2. KONFIGURASI AWAL & MUAT MODEL AI (PAKAI VERSI LEBIH AKURAT) ===
# Pakai model ukuran MENENGAH, lebih pintar baca benda kecil/tertutup
model = YOLO("yolov8m.pt")  

# === 3. PENGATURAN TAMPILAN APLIKASI ===
st.set_page_config(
    page_title="Pendeteksi Benda AI | Kurniadi Wira Kusuma",
    page_icon="🔍",
    layout="wide"
)

# Judul Utama
st.title("🔍 SISTEM PENDETEKSI BENDA - KECERDASAN BUATAN")
st.markdown("""
> ✅ Teknologi: YOLOv8 | Tingkat Akurasi Ditingkatkan | Mendeteksi 80+ Jenis Benda
> 📌 Fungsi: Mendeteksi, menandai, menghitung, dan menampilkan tingkat kepercayaan benda dalam gambar.
> Cocok untuk pengembangan sistem keamanan, kendaraan pintar, dan analisis visual.
""")
st.divider()

# === 4. BIDANG UNGGAH GAMBAR ===
unggah_gambar = st.file_uploader("📤 Silakan Pilih Gambar / Foto", type=["jpg", "jpeg", "png"])

if unggah_gambar is not None:
    # Buka dan tampilkan gambar asli
    gambar_asli = Image.open(unggah_gambar)
    
    # Bagi tampilan jadi dua kolom
    kolom_kiri, kolom_kanan = st.columns(2)
    
    with kolom_kiri:
        st.subheader("🖼️ GAMBAR ASLI")
        st.image(gambar_asli, use_column_width=True)

    with kolom_kanan:
        st.subheader("🤖 HASIL DETEKSI SISTEM AI")
        with st.spinner("⏳ Sedang memindai... Sistem bekerja lebih teliti, mohon tunggu sebentar..."):
            
            # === 5. PENGATURAN DETEKSI YANG DIPERBAIKI ===
            # ⚙️ PERUBAHAN PENTING: Turunkan batas akurasi jadi 0.25 / 25% 
            # Biar benda kecil, jauh, agak tertutup MASIH TERBACA & TERDETEKSI
            hasil = model(gambar_asli, conf=0.25, iou=0.45, verbose=False)

            # Gambar kotak dan tulisan nama benda + PERSENTASE AKURASI
            gambar_hasil = hasil[0].plot()
            
            # Perbaiki susunan warna biar warnanya pas
            gambar_hasil = cv2.cvtColor(gambar_hasil, cv2.COLOR_BGR2RGB)
            
            # Tampilkan hasil akhir
            st.image(gambar_hasil, use_column_width=True)

    st.divider()

    # === 6. TAMPILKAN RINCIAN HASIL DETEKSI (LEBIH LENGKAP) ===
    st.subheader("📋 RINCIAN LENGKAP HASIL PEMINDAIAN")
    
    daftar_id = hasil[0].boxes.cls
    daftar_nama = hasil[0].names
    nilai_akurasi = hasil[0].boxes.conf  # Ambil data persentase keakuratan
    jumlah_benda = {}
    daftar_rincian = []

    # Hitung jumlah dan kumpulkan data
    for i, id_kelas in enumerate(daftar_id):
        nama = daftar_nama[int(id_kelas)]
        akurasi = round(float(nilai_akurasi[i]) * 100, 1) # Ubah jadi persen
        jumlah_benda[nama] = jumlah_benda.get(nama, 0) + 1
        daftar_rincian.append(f"• {nama} : Tingkat keakuratan {akurasi}%")

    # Tampilkan ringkasan jumlah
    if jumlah_benda:
        st.markdown("**📊 JUMLAH BENDA DITEMUKAN:**")
        total_semua = 0
        for nama, banyaknya in jumlah_benda.items():
            st.success(f"✅ **{nama}** : {banyaknya} buah")
            total_semua += banyaknya

        st.info(f"📌 **TOTAL SELURUH BENDA : {total_semua} BUAH**")

        st.markdown("---")
        st.markdown("**🔎 RINCIAN DETEKSI PER OBJEK:**")
        for rincian in daftar_rincian:
            st.write(rincian)

    else:
        st.warning("⚠️ Tidak ada benda yang dikenali dalam gambar ini.")

    st.balloons()
    st.markdown("**🎉 Selesai! Sistem berjalan sukses dengan pengaturan akurasi ditingkatkan.**")

else:
    st.info("👉 Silakan unggah gambar terlebih dahulu untuk memulai pendeteksian.")