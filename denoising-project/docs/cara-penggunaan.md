# 🚀 CARA MENGGUNAKAN PROGRAM DENOISING

## 📋 LANGKAH 1: SIAPIN FILE
Pastikan kamu punya file-file ini dalam satu folder:

```folder-kamu/
├── denoising.py ← File program utama
├── gambar 1.jpg ← Gambar yang mau dibersihin
└── requirements.txt ← Daftar library
```

**Note:** Ganti `gambar 1.jpg` dengan foto yang mau kamu bersihin.

## 🛠️ LANGKAH 2: INSTALL OPENCV
Buka **Command Prompt** atau **Terminal**, lalu ketik:

```bash
pip install opencv-python
Kalo udah berhasil, harusnya muncul tulisan Successfully installed opencv-python...
```

## 🎮 LANGKAH 3: JALANKAN PROGRAM
Masih di Command Prompt, ketik:

```bash
python denoising.py
```

## 👀 APA YANG TERJADI SELANJUTNY?
Program baca gambar gambar 1.jpg

Proses denoising berjalan (tunggu beberapa detik)

Muncul 2 window:

"Original" = gambar sebelum

"Denoised" = gambar sesudah

File hasil disimpan sebagai foto_denoised.jpg

## 🖱️ LANGKAH 4: LIHAT HASIL
- Klik window manapun

- Tekan tombol keyboard apa aja (spasi, enter, esc)

- Program tutup dan selesai!

## 📁 HASIL YANG DIDAPAT

-- foto_denoised.jpg - Gambar yang udah dibersihin

-- Bandingin sama gambar asli, harusnya lebih bersih dan halus

⚡ MAU COBA GAMBAR LAIN?
Ganti nama file gambar kamu jadi gambar 1.jpg atau edit kodenya:

python
# Ganti "gambar 1.jpg" dengan nama file kamu
img = cv2.imread("foto-saya.jpg")
🎛️ MAU ATUR KEKUATAN DENOISING?
Edit parameter h di kode:

python
# Untuk noise dikit: h=5-10
# Untuk noise banyak: h=20-30
denoised = cv2.fastNlMeansDenoising(gray, None, h=15, ...)
❌ KALAU ERROR?
Cek Troubleshooting atau:

Pastikan file gambar 1.jpg ada di folder yang bener

Pastikan OpenCV udah keinstall

Pastikan namanya "gambar 1.jpg" (ada spasinya)

🎉 SELAMAT! Gambar kamu sekarang seharusnya udah lebih bersih dari noise!

⬅️ Kembali ke Penjelasan Utama

text

## 🎯 **POIN-POIN PENTING YANG DIMASUKIN:**

### ✅ **Yang ADA:**
- **Step-by-step yang jelas** (1-2-3-4)
- **Command yang bisa dicopy-paste**
- **Visualisasi** (folder structure)
- **Expectation management** (apa yang akan terjadi)
- **Tips praktis** (ganti gambar, atur parameter)
- **Troubleshooting cepat**

### ❌ **Yang TIDAK ADA:**
- Penjelasan teori algoritma
- Dokumentasi fungsi teknis  
- Solusi error detail
- Background programming

## 🚀 **USER JOURNEY-nya:**
1. User baca → paham dalam 2 menit
2. Copy-paste command → works!
3. Lihat hasil → seneng!
4. Mau advanced? → ada tips sederhana

**Gitu aja bro, simpel dan praktis!** User langsung bisa jalanin tanpa pusing baca dokumentasi teknis. 😊

