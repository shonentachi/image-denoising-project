# 📊 Dokumentasi Teknis - Image Denoising

## 🎯 Overview
Proyek ini mengimplementasikan algoritma **Non-Local Means Denoising** menggunakan OpenCV untuk mengurangi noise pada gambar digital.

## 🔬 Algoritma yang Digunakan

### Non-Local Means Denoising
- **Konsep**: Memanfaatkan similarity antara patch gambar
- **Keunggulan**: Mempertahankan detail edges dan texture
- **Kompleksitas**: O(n²) tetapi efektif untuk quality

### Parameter Algoritma:
```python
h = 10                    # Filter strength
templateWindowSize = 7    # Patch size untuk perbandingan
searchWindowSize = 21     # Area pencarian similarity