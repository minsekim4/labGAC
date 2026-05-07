import numpy as np
import cv2
from matplotlib import pyplot as plt

# 1. Citirea imaginii
img_bgr = cv2.imread("flori.png")
if img_bgr is None:
    print("Couldn't open the image")

# Am mărit puțin factorul de redimensionare (fx=0.3, fy=0.3) 
# pentru a putea observa mai bine efectele filtrelor.
img_bgr = cv2.resize(img_bgr, (0, 0), fx=0.3, fy=0.3)

# 2. Conversie BGR -> RGB pentru afișarea corectă a culorilor în Matplotlib
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# ==========================================
# FILTRE DE ESTOMPARE (BLURRING) & ZGOMOT
# ==========================================

# A. Box Blur (Implementarea ta manuală)
ker_size = 5
kernel_box = np.ones((ker_size, ker_size), dtype=np.float32) / ker_size**2
res_box = cv2.filter2D(img_rgb, -1, kernel_box, (-1,-1), delta=0, borderType=cv2.BORDER_DEFAULT)

# B. Gaussian Blur
res_gaussian = cv2.GaussianBlur(img_rgb, (5, 5), 0, 0)

# C. Median Blur (Setează dimensiunea kernelului la 5)
res_median = cv2.medianBlur(img_rgb, 5)

# D. Bilateral Filter 
# Parametri: src, diametru=15, sigmaColor=80, sigmaSpace=80
res_bilateral = cv2.bilateralFilter(img_rgb, 15, 80, 80)

# ==========================================
# FILTRE PENTRU MARGINI (EDGES & SHARPENING)
# ==========================================

# E. Image Sharpening (Accentuare margini)
sharpen_kernel = np.array([[0, -1, 0], 
                           [-1, 5, -1], 
                           [0, -1, 0]], dtype="int")
res_sharpen = cv2.filter2D(img_rgb, -1, sharpen_kernel)

# F. Laplacian Filter (Extragere Contururi)
# Laplacian funcționează cel mai bine pe imagini Grayscale
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
# 1. Blur Gaussian pentru reducerea zgomotului
img_gray_blurred = cv2.GaussianBlur(img_gray, (3, 3), 0)
# 2. Aplicare filtru cu ddepth = CV_32F
res_laplacian = cv2.Laplacian(img_gray_blurred, cv2.CV_32F)
# 3. Normalizare între 0 și 1
res_laplacian = cv2.normalize(res_laplacian, None, 0, 1, cv2.NORM_MINMAX, dtype=cv2.CV_32F)

# ==========================================
# AFIȘAREA REZULTATELOR
# ==========================================

plt.figure(figsize=(15, 10))

plt.subplot(231)
plt.imshow(img_rgb)
plt.title("Originală (RGB)")
plt.axis('off')

plt.subplot(232)
plt.imshow(res_box)
plt.title("Box Blur (Filtru Manual)")
plt.axis('off')

plt.subplot(233)
plt.imshow(res_gaussian)
plt.title("Gaussian Blur 5x5")
plt.axis('off')

plt.subplot(234)
plt.imshow(res_median)
plt.title("Median Blur 5")
plt.axis('off')

plt.subplot(235)
plt.imshow(res_bilateral)
plt.title("Bilateral Filter")
plt.axis('off')

plt.subplot(236)
plt.imshow(res_sharpen)
plt.title("Sharpen Filter")
plt.axis('off')

plt.tight_layout()
plt.show()

# Afișare separată pentru Laplacian (deoarece este imagine 2D Grayscale)
plt.figure(figsize=(6, 5))
plt.imshow(res_laplacian, cmap='gray')
plt.title("Laplacian Edge Detection (Grayscale)")
plt.axis('off')
plt.show()