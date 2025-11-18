# 📊 PENJELASAN TEKNIS DENOISING GAMBAR

## 🎯 APA ITU DENOISING?
Denoising adalah proses **menghilangkan noise** (gangguan) dari gambar sehingga gambar menjadi lebih bersih dan jelas.

**Analoginya:** Seperti membersihkan foto lama yang berdebu dan bekas goresan.

## 🔬 ALGORITMA YANG DIGUNAKAN

### Non-Local Means Denoising
Algoritma ini bekerja dengan cara **membandingkan bagian-bagian gambar** yang mirip di seluruh area gambar.

**Cara kerjanya:**
- Ambil satu bagian kecil gambar (patch)
- Cari bagian-bagian lain di gambar yang mirip
- Rata-ratakan bagian-bagian yang mirip tersebut
- Hasil rata-rata digunakan untuk membersihkan noise

**Keunggulan:**
- ✅ Mempertahankan ketajaman edges
- ✅ Tidak membuat gambar blur
- ✅ Efektif untuk berbagai jenis noise

## ⚙️ PARAMETER-PARAMETER TEKNIS

```python
# Parameter dalam kode kita:
h = 10                    # Kekuatan filter (3-30)
templateWindowSize = 7    # Ukuran patch untuk perbandingan
searchWindowSize = 21     # Area pencarian similarity
