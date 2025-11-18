# 🔌 API REFERENCE - DOKUMENTASI FUNGSI

## 📋 DAFTAR FUNGSI

### 🔹 `cv2.imread()`
**Fungsi:** Membaca gambar dari file

```python
img = cv2.imread("nama_file.jpg")
```

Parameters:

- filename (string): Path dan nama file gambar

- flags (optional): Cara baca gambar (default: cv2.IMREAD_COLOR)

Return:

numpy array atau None jika gagal

Contoh:

```python
# Baca gambar normal
img = cv2.imread("gambar.jpg")

# Baca gambar grayscale langsung
img = cv2.imread("gambar.jpg", cv2.IMREAD_GRAYSCALE)
```

Flags yang tersedia:

- cv2.IMREAD_COLOR → BGR color (default)

- cv2.IMREAD_GRAYSCALE → Grayscale

- cv2.IMREAD_UNCHANGED → Dengan alpha channel

##🔹 cv2.cvtColor()
Fungsi: Mengkonversi warna gambar

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
Parameters:

- src (numpy array): Gambar input

- code (constant): Kode konversi warna

Return:

- numpy array: Gambar hasil konversi

Color Conversion Codes:

- cv2.COLOR_BGR2GRAY → BGR ke Grayscale

- cv2.COLOR_BGR2RGB → BGR ke RGB

- cv2.COLOR_BGR2HSV → BGR ke HSV

Contoh:

```python
# BGR ke Grayscale (yang kita pakai)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR ke RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
## 🔹 cv2.fastNlMeansDenoising()

Fungsi: Denoising gambar grayscale

```python
denoised = cv2.fastNlMeansDenoising(
    gray, 
    None, 
    h=10, 
    templateWindowSize=7, 
    searchWindowSize=21
)
```
Parameters:

- src (numpy array): Gambar grayscale input

- dst (numpy array): Output (bisa None)

- h (float): Parameter kekuatan filter (3-30)

- templateWindowSize (int): Ukuran template window (3,5,7)

- searchWindowSize (int): Ukuran search window (harus ganjil)

Return:

- numpy array: Gambar hasil denoising

Contoh Parameter Combinations:

```python
# Mild denoising
denoised = cv2.fastNlMeansDenoising(gray, None, h=5, templateWindowSize=5, searchWindowSize=15)

# Strong denoising  
denoised = cv2.fastNlMeansDenoising(gray, None, h=25, templateWindowSize=7, searchWindowSize=25)
```

🔹 cv2.imwrite()
Fungsi: Menyimpan gambar ke file

```python
cv2.imwrite("output.jpg", denoised)
```
Parameters:

- filename (string): Nama file output

- img (numpy array): Gambar yang akan disimpan

- params (optional): Parameter kualitas (untuk JPEG)

Return:

- bool: True jika sukses, False jika gagal

Contoh:

```python
# Simpan biasa
cv2.imwrite("hasil.jpg", denoised)

# Simpan dengan kualitas JPEG
cv2.imwrite("hasil.jpg", denoised, [cv2.IMWRITE_JPEG_QUALITY, 95])
```

###   🔹 cv2.imshow()
Fungsi: Menampilkan gambar di window

```python
cv2.imshow("Window Title", image)
```

Parameters:

- winname (string): Nama window

- mat (numpy array): Gambar yang akan ditampilkan

Contoh:

```python
# Tampilkan satu gambar
cv2.imshow("My Image", img)

# Tampilkan multiple gambar
cv2.imshow("Original", gray)
cv2.imshow("Denoised", denoised)
```

### 🔹 cv2.waitKey()
Fungsi: Menunggu input keyboard

```python
cv2.waitKey(0)
```
Parameters:

- delay (int): Delay dalam milisecond

- 0 = Tunggu tanpa timeout

- >0 = Tunggu selama X ms

Return:

- int: ASCII code tombol yang ditekan, atau -1 jika timeout

Contoh:

```python
# Tunggu sampai user tekan tombol
key = cv2.waitKey(0)

# Tunggu 5 detik, lalu lanjut
key = cv2.waitKey(5000)
```

### 🔹 cv2.destroyAllWindows()
Fungsi: Menutup semua window OpenCV

```python
cv2.destroyAllWindows()
```
Parameters: Tidak ada

Contoh:

```python
# Tutup semua window
cv2.destroyAllWindows()

# Tutup window spesifik
cv2.destroyWindow("Window Title")
```
💻 CODE STRUCTURE LENGKAP
Program Utama Kita:
```python
import cv2

# 1. Baca gambar
img = cv2.imread("gambar 1.jpg")

# 2. Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Denoising
denoised = cv2.fastNlMeansDenoising(gray, None, h=10, templateWindowSize=7, searchWindowSize=21)

# 4. Simpan hasil
cv2.imwrite("foto_denoised.jpg", denoised)

# 5. Tampilkan perbandingan
cv2.imshow("Original", gray)
cv2.imshow("Denoised", denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## 🛠️ EXTENSION FUNCTIONS
Untuk Color Denoising:
```python
# Denoising gambar berwarna
denoised_color = cv2.fastNlMeansDenoisingColored(
    img, 
    None, 
    h=10, 
    hColor=10, 
    templateWindowSize=7, 
    searchWindowSize=21
)
Untuk Multiple Images:
python
# Denoising multiple gambar
denoised_multi = cv2.fastNlMeansDenoisingMulti(
    [img1, img2, img3], 
    imgIndex=1, 
    temporalWindowSize=3,
    h=10,
    templateWindowSize=7,
    searchWindowSize=21
)
```
## 🎯 ERROR HANDLING
Contoh dengan Error Handling:
```python
import cv2

try:
    # Baca gambar
    img = cv2.imread("gambar.jpg")
    if img is None:
        raise FileNotFoundError("Gambar tidak ditemukan")
    
    # Konversi warna
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Denoising
    denoised = cv2.fastNlMeansDenoising(gray, None, h=10)
    
    # Simpan hasil
    success = cv2.imwrite("hasil.jpg", denoised)
    if not success:
        raise IOError("Gagal menyimpan gambar")
        
    print("Proses selesai sukses!")
    
except Exception as e:
    print(f"Error: {e}")
```
🔧 TIPS DEVELOPMENT
Debugging Image Properties:
```python
# Cek properti gambar
print(f"Shape: {img.shape}")        # (height, width, channels)
print(f"Size: {img.size}")          # Total pixels
print(f"Dtype: {img.dtype}")        # Data type
print(f"Min: {img.min()}, Max: {img.max()}")  # Value range
Performance Monitoring:
python
import time

start_time = time.time()

# Proses denoising
denoised = cv2.fastNlMeansDenoising(gray, None, h=10)

end_time = time.time()
print(f"Processing time: {end_time - start_time:.2f} seconds")
