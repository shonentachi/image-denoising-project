import cv2

# === 1. Load gambar ===
img = cv2.imread("gambar 1.jpg")

if img is None:
    print("Gambar tidak ditemukan. Pastikan nama file benar!")
    exit()

# === 2. Konversi ke grayscale (opsional tapi lebih jelas perubahannya) ===
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# === 3. Denoising ===
denoised = cv2.fastNlMeansDenoising(gray, None, h=10, templateWindowSize=7, searchWindowSize=21)

# === 4. Simpan hasil ===
cv2.imwrite("foto_denoised.jpg", denoised)

# === 5. Tampilkan sebelum-sesudah ===
cv2.imshow("Original", gray)
cv2.imshow("Denoised", denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()
