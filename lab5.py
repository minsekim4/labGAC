import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('flori.png',0)
img2 = cv2.imread('flori.png',1)
imagine_afisare1 = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
imagine_afisare2 = cv2.resize(img2, (0, 0), fx=0.1, fy=0.1)
cv2.imshow('img',imagine_afisare1)
cv2.imshow('img_color',imagine_afisare2)
k=cv2.waitKey(0)
k=cv2.waitKey(0)

img3 = cv2.imread('flori.png',0)
img3 = cv2.resize(img3, (0,0), fx=0.2, fy=0.2)
cv2.imshow('img3',img3)
k=cv2.waitKey(0)
if k == 27: #w8 for ESC to exit
    cv2.destroyAllWindows()
elif k == ord('s'): #w8 for s to save and exit
    cv2.imwrite('florigray2.png',img3)


img4 = cv2.imread('flori.png',1)
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)
img4 = cv2.resize(img4, (0, 0), fx=0.1, fy=0.1)
cv2.imshow('img4',img4)
k=cv2.waitKey(0)

img5 = cv2.imread('flori.png',1)
img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2YCrCb)
img5 = cv2.resize(img5, (0, 0), fx=0.1, fy=0.1)
cv2.imshow('img5',img5)
k=cv2.waitKey(0)

img6 = cv2.imread('flori.png',1)
img6 = cv2.resize(img6, (0, 0), fx=0.1, fy=0.1)
img6_rgb = cv2.cvtColor(img6, cv2.COLOR_BGR2RGB)
plt.figure(figsize=[10,5])
plt.imshow(img6_rgb)
plt.title("imagine originala RGB")
plt.axis('off')
plt.show()
hsvimg6 = cv2.cvtColor(img6, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(hsvimg6)
H_array = H[S>10].flatten()

print(f"forma canalului H: {H.shape}")
print(f"Număr de pixeli filtrați: {H_array.shape}")

plt.figure(figsize=[12,5])
plt.subplot(121)
plt.imshow(img6_rgb)
plt.title("Imagine")
plt.axis('off')

plt.subplot(122)
plt.hist(H_array, bins=180, color='r', range=[0, 180])
plt.title("Histogram")
plt.xlabel("Nuanta (0-179)")
plt.ylabel("Nr. Pixeli")
plt.show()