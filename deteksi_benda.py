# ==================================================
# PROYEK : SISTEM PENDETEKSI & PENGHITUNG OBJEK CERDAS
# TEKNOLOGI : PYTHON + YOLOv8 + OpenCV + Streamlit
# VERSI : 3.0 ✅ PALING AKURAT ✅ SEMUA TERBACA ✅
# DIBUAT OLEH : Kurniadi Wira Kusuma
# ==================================================

# === 1. IMPOR ALAT ===
from ultralytics import YOLO   
import cv2                      
import streamlit as st         
from PIL import Image
import numpy as np

# === 2. MUAT MODEL PALING BAGUS ===
# Pakai yolov8m = lebih pintar dari versi biasa, jago baca bentuk tidak lengkap
model = YOLO("yolov8m.pt")  

# === 3. PENGATURAN TAMPILAN ===
st.set_page_config(
    page_title="Pendeteksi Objek AI | Kurniadi Wira Kusuma",
    page_icon="🔍",
    layout="wide"
)

# Judul
st.title("🔍 SISTEM PENDETEKSI DAN PENGHITUNG OBJEK CERDAS - AI")
st.markdown("""
> ✅ Teknologi: YOLOv8 | Tingkat Kepekaan Ditingkatkan MAKSIMAL
> 📌 Fungsi: Mendeteksi objek walaupun tertutup sebagian, jauh, miring atau agak gelap
> 🎯 Cocok untuk: Industri, pabrik, penghitungan produksi, pengawasan
""")
st.divider()

# === 4. BIDANG UNGGAH GAMBAR ===
unggah_gambar = st.file_uploader("📤 Masukkan Gambar / Foto", type=["jpg", "jpeg", "png"])

if unggah_gambar is not None:
    gambar_asli = Image.open(unggah_gambar)
    kolom_kiri, kolom_kanan = st.columns(2)
    
    with kolom_kiri:
        st.subheader("🖼️ GAMBAR ASLI")
        st.image(gambar_asli, use_column_width=True)

    with kolom_kanan:
        st.subheader("🤖 HASIL DETEKSI SISTEM AI")
        with st.spinner("⏳ Memindai... Kepekaan MAKSIMAL, semua objek akan dibaca..."):
            
            # ⚙️ PENGATURAN KUNCINYA ✅ DIPERBAIKI TOTAL ✅
            # conf=0.15 → CUKUP YAKIN 15% AJA LANGSUNG DIBACA! (Dulu 25%, sekarang makin peka)
            # iou=0.3   → Biar yang ketindihan/ketutup tetap dibaca terpisah
            # agnostic_nms=True → Jangan gabungkan kotak, biar semua muncul
            hasil = model(
                gambar_asli, 
                conf=0.15,     
                iou=0.3,       
                agnostic_nms=True,
                verbose=False
            )

            gambar_hasil = hasil[0].plot()
            gambar_hasil = cv2.cvtColor(gambar_hasil, cv2.COLOR_BGR2RGB)
            st.image(gambar_hasil, use_column_width=True)

    st.divider()

    # === 5. RINCIAN HASIL ===
    st.subheader("📋 RINCIAN LENGKAP HASIL PEMINDAIAN")
    
    daftar_id = hasil[0].boxes.cls
    daftar_nama = hasil[0].names
    nilai_akurasi = hasil[0].boxes.conf
    jumlah_benda = {}
    daftar_rincian = []

    # Hitung dan kumpulkan semua data
    for i, id_kelas in enumerate(daftar_id):
        nama = daftar_nama[int(id_kelas)]
        akurasi = round(float(nilai_akurasi[i]) * 100, 1)
        jumlah_benda[nama] = jumlah_benda.get(nama, 0) + 1
        daftar_rincian.append(f"• {nama} : {akurasi}%")

    # Tampilkan ringkasan
    if jumlah_benda:
        st.markdown("**📊 JUMLAH OBJEK DITEMUKAN:**")
        total_semua = 0
        for nama, banyaknya in jumlah_benda.items():
            # Khusus tulis ORANG biar jelas banget
            if nama == "person":
                st.success(f"✅ **JUMLAH ORANG : {banyaknya} ORANG**")
            else:
                st.info(f"ℹ️ **{nama} : {banyaknya} buah**")
            total_semua += banyaknya

        st.success(f"📌 **TOTAL SELURUH OBJEK TERDETEKSI : {total_semua} BUAH**")

        st.markdown("---")
        st.markdown("**🔎 DETAIL TIAP OBJEK:**")
        for rincian in daftar_rincian:
            st.write(rincian)

    else:
        st.warning("⚠️ Tidak ada objek terdeteksi.")

    st.balloons()
    st.markdown("**✅ VERSI 3.0 : KEPEKAAN MAKSIMAL - SEMUA OBJEK DIBACA**")

else:
    st.info("👉 Silakan unggah gambar dulu ya.")