# 🔬 PENJELASAN TEKNIS DENOISING

## 🧠 KONSEP DASAR DENOISING

### Apa itu Noise?
**Noise** = gangguan/granularitas dalam gambar yang bikin tampilan jadi tidak smooth.

**Contoh noise:**
- Foto low-light (ISO tinggi)
- Foto hasil scan dokumen lama
- Gambar dari sensor kamera murah

### Kenapa Perlu Denoising?
- **Meningkatkan kualitas visual**
- **Mempermudah analisis gambar** (untuk computer vision)
- **Memperbaiki gambar rusak**

## ⚙️ ALGORITMA NON-LOCAL MEANS

### Cara Kerja Simple-nya:

```python
# Analogi:
for setiap_pixel_di_gambar:
    cari_pixel_mirip_di_seluruh_gambar()
    hitung_rata_rata_pixel_mirip()
    ganti_pixel_dengan_hasil_rata_rata()
```

### Bedanya dengan Denoising Biasa:
- Traditional: Cuma lihat tetangga dekat → hasil blur

- Non-Local Means: Lihat seluruh gambar → hasil lebih natural

### 📊 PARAMETER TEKNIS
1. h (Filter Strength)
```python
h = 10  # Nilai default
```
Fungsi: Mengatur kekuatan denoising

Range values:

- h = 3-10 → Denoising lembut (good for mild noise)

- h = 10-20 → Denoising medium (balanced)

- h = 20-30 → Denoising kuat (heavy noise)

Efek:

- h kecil → Noise masih sisa, detail terjaga

- h besar → Noise hilang, mungkin detail ikut hilang

2. templateWindowSize
```python
templateWindowSize = 7  # Harus ganjil!
Fungsi: Ukuran patch kecil yang dibandingkan
```
Allowed values: 3, 5, 7

Efek:

- Nilai kecil (3) → Lebih detail, lebih lambat

- Nilai besar (7) → Lebih smooth, lebih cepat

3. searchWindowSize
```python
searchWindowSize = 21  # Harus ganjil!
Fungsi: Seberapa luas area pencarian pixel mirip
```
Allowed values: 15, 21, 25, 31

Efek:

- Nilai kecil → Cepat, hasil kurang optimal

- Nilai besar → Lambat, hasil lebih bagus

### 🔍 DETAIL IMPLEMENTASI
Flow Program Kita:
```python
# 1. Baca gambar
img = cv2.imread("gambar 1.jpg")           # BGR format

# 2. Konversi ke grayscale  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Optimasi processing

# 3. Apply denoising
denoised = cv2.fastNlMeansDenoising(gray, None, h=10, ...)

# 4. Save & show results
cv2.imwrite("hasil.jpg", denoised)
```

Kenapa Pakai Grayscale?
Lebih cepat → 1 channel vs 3 channels (RGB)

Noise lebih mudah diidentifikasi

Hasil lebih konsisten

## 📈 METRIK KUALITAS
PSNR (Peak Signal-to-Noise Ratio)
Rumus: PSNR = 20 * log10(MAX / √MSE)

Interpretasi:

- PSNR < 20 dB → Poor quality

- PSNR 20-30 dB → Acceptable

- PSNR > 30 dB → Good quality

- PSNR > 40 dB → Excellent

Improvement Typical:
Gambar noisy ringan: +5-10 dB improvement

Gambar noisy berat: +10-15 dB improvement

### 🆚 PERBANDINGAN ALGORITMA

Non-Local Means vs Others:
```Markdown
Algorithm	Kelebihan	Kekurangan
Non-Local Means	Hasil natural, detail terjaga	Processing lambat
Gaussian Blur	Cepat	Hasil blur, detail hilang
Median Filter	Bagus untuk salt-pepper noise	Tidak optimal untuk Gaussian noise
Bilateral Filter	Pertahankan edges	Parameter sensitif
```
## 🎯 OPTIMAL PARAMETER COMBINATIONS
Untuk Various Scenarios:
1. Portrait Photos (Skin Smoothing)
```python
h = 8, templateWindowSize = 5, searchWindowSize = 15
→ Pertahankan detail wajah, hilangkan noise halus
```

2. Document Scanning
```python
h = 15, templateWindowSize = 7, searchWindowSize = 21  
→ Hilangkan noise berat, pertahankan text clarity
```

3. Low-light Photography
```python
h = 25, templateWindowSize = 7, searchWindowSize = 25
→ Strong denoising untuk high ISO noise
```

### ⚠️ LIMITASI & SOLUSI
Limitations:
Processing time lama untuk gambar besar

Memory intensive untuk high resolution

Tidak optimal untuk structured noise

Workarounds:
```python
# Untuk gambar besar, resize dulu
img = cv2.imread("large_image.jpg")
img_small = cv2.resize(img, (1200, 800))  # Resize dulu
```

## 🔬 ADVANCED TOPICS
Color Image Denoising:
```python
# Bisa juge denoise color image langsung
denoised_color = cv2.fastNlMeansDenoisingColored(img, None, h=10, ...)
Multiple Iterations:
```
```python
# Denoising berulang untuk hasil lebih halus
denoised1 = cv2.fastNlMeansDenoising(gray, None, h=10, ...)
denoised2 = cv2.fastNlMeansDenoising(denoised1, None, h=5, ...)
