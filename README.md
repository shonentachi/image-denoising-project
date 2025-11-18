# Image Denoising dengan OpenCV

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)

Proyek ini implementasi algoritma **Non-Local Means Denoising** untuk mengurangi noise pada gambar menggunakan library OpenCV.

## 📋 Fitur
* ✅ Denoising gambar grayscale
* ✅ Perbandingan visual sebelum & sesudah
* ✅ Export hasil processing
* ✅ Parameter yang dapat disesuaikan

## 🛠️ Instalasi

### Prerequisites
* Python 3.6+
* OpenCV

## 📋 Fitur 

```bash
pip install opencv-python

```

###🚀 Cara Menggunakan
Siapkan gambar di folder images/original/

## 📋 Fitur

```bash
cd src
python denoising.py
Hasil akan tersimpan di images/results/
```

## 📁 Struktur Project

```text
denoising-project/
├── src/                    # Source code
│   ├── denoising.py       # Main script
│   └── requirements.txt   # Dependencies
├── images/                # Folder gambar
│   ├── original/         # Gambar input
│   └── results/          # Hasil denoising
├── docs/                 # Dokumentasi
└── README.md            # File ini
```

##3⚙️ Parameter Denoising

```python
# Default parameters:
h = 10                   # Kekuatan filter
templateWindowSize = 7   # Ukuran template window  
searchWindowSize = 21    # Ukuran search window
```

##📸 Contoh Hasil

before
[https://github.com/shonentachi/image-denoising-project/blob/main/denoising-project/images/original/gambar%201.jpg]


after
[https://github.com/shonentachi/image-denoising-project/blob/main/denoising-project/images/results/foto_denoised.jpg]

##🎯 Teknik yang Digunakan

Non-Local Means Denoising: Algoritma canggih yang mempertahankan detail gambar

Grayscale Conversion: Optimasi processing

Real-time Comparison: Visualisasi langsung

##👨‍💻 Author

Dibuat oleh [Egy Fahmi Ramadhani]

##📄 License

MIT License - bebas digunakan untuk project personal maupun komersial.

text
## 📄 File requirements.txt
```'txt
opencv-python==4.8.1.78
```

##🔧 Modified Code dengan Path yang Lebih Baik
```python
import cv2
import os

def create_folders():
    """Membuat folder jika belum ada"""
    folders = ['../images/original', '../images/results']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def denoise_image():
    # === 1. Load gambar ===
    img_path = "../images/original/gambar 1.jpg"
    img = cv2.imread(img_path)

    if img is None:
        print(f"Gambar tidak ditemukan di: {img_path}")
        print("Pastikan file 'gambar 1.jpg' ada di folder images/original/")
        return

    # === 2. Konversi ke grayscale ===
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # === 3. Denoising ===
    denoised = cv2.fastNlMeansDenoising(gray, None, h=10, templateWindowSize=7, searchWindowSize=21)

    # === 4. Simpan hasil ===
    output_path = "../images/results/foto_denoised.jpg"
    cv2.imwrite(output_path, denoised)
    print(f"Hasil denoising disimpan di: {output_path}")

    # === 5. Tampilkan sebelum-sesudah ===
    cv2.imshow("Original", gray)
    cv2.imshow("Denoised", denoised)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    create_folders()
    denoise_image()
