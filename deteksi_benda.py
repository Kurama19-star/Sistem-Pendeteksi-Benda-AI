# ==================================================
# PROYEK : SISTEM PENDETEKSI BENDA DALAM GAMBAR
# TEKNOLOGI : PYTHON + ULTRALYTICS + YOLOv8
# DESKRIPSI : Aplikasi AI untuk mengenali dan menandai 
#             benda-benda yang ada di dalam gambar/foto
# DIBUAT OLEH : Kurama19-star
# ==================================================

# === 1. IMPOR SEMUA ALAT DAN PUSTAKA ===
from ultralytics import YOLO   # Otak Kecerdasan Buatan (Model YOLO)
import cv2                      # Perpustakaan pengolahan gambar
import streamlit as st          # Alat pembuat tampilan aplikasi web
from PIL import Image           # Alat pembuka berkas gambar

# === 2. KONFIGURASI AWAL & MUAT MODEL AI ===
model = YOLO("yolov8m.pt")

# === 3. PENGATURAN TAMPILAN APLIKASI ===
st.set_page_config(
    page_title="Pendeteksi Benda AI",
    page_icon="🔍",
    layout="wide"
)

# Judul Utama
st.title("🔍 PENDETEKSI BENDA DALAM GAMBAR - KECERDASAN BUATAN")
st.markdown("""
> 📌 Unggah foto atau gambar apa saja, sistem kecerdasan buatan akan secara otomatis 
> memindai, mengenali, menandai, dan menghitung benda-benda yang ada di dalamnya.
> Teknologi: **YOLOv8 | Penglihatan Komputer**
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
        st.subheader("🤖 HASIL DETEKSI AI")
        with st.spinner("⏳ Sedang memindai gambar, mohon tunggu sebentar..."):
            
            # === 5. PROSES KERJA KECERDASAN BUATAN ===
            hasil = model(gambar_asli, conf=0.5, verbose=False)

            # Gambar kotak dan tulisan nama benda secara otomatis
            gambar_hasil = hasil[0].plot()
            
            # Perbaiki susunan warna biar warnanya pas
            gambar_hasil = cv2.cvtColor(gambar_hasil, cv2.COLOR_BGR2RGB)
            
            # Tampilkan hasil akhir
            st.image(gambar_hasil, use_column_width=True)

    st.divider()

    # === 6. TAMPILKAN DAFTAR RINCI HASIL DETEKSI ===
    st.subheader("📋 RINCIAN BENDA YANG DITEMUKAN")
    
    daftar_id = hasil[0].boxes.cls
    daftar_nama = hasil[0].names
    jumlah_benda = {}

    for id_kelas in daftar_id:
        nama = daftar_nama[int(id_kelas)]
        jumlah_benda[nama] = jumlah_benda.get(nama, 0) + 1

    if jumlah_benda:
        for nama, banyaknya in jumlah_benda.items():
            st.success(f"✅ **{nama}** : {banyaknya} buah ditemukan")
    else:
        st.warning("⚠️ Tidak ada benda yang dikenali dalam gambar ini.")

    st.balloons()
    st.markdown("**🎉 Selesai! Sistem pendeteksian berjalan dengan sukses.**")

else:
    st.info("👉 Silakan unggah gambar terlebih dahulu untuk memulai pendeteksian.")