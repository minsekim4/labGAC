import numpy as np
import cv2
from matplotlib import pyplot as plt


img =cv2.imread("flori.png")
img_bgr = cv2.resize(img_bgr, (0, 0), fx=0.3, fy=0.3)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

if img is None:
    print("Couldn't open the image")
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
ker_size = 5
kernel = np.ones((ker_size, ker_size), dtype=np.float32)/ker_size**2
print(kernel)
result = cv2.filter2D(img, -1, kernel, (-1,-1), delta=0, borderType=cv2.BORDER_DEFAULT)
plt.figure()
plt.subplot(121)
plt.imshow(img)
plt.title("original")
plt.subplot(122)
plt.imshow(result)
plt.title("result")
plt.show()


