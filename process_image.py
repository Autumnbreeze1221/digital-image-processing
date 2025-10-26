import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

img = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.rectangle(img, (50, 50), (250, 250), (0, 255, 0), -1)
cv2.circle(img, (150, 150), 60, (255, 0, 0), -1)
cv2.putText(img, "DIP", (90, 160), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imwrite("images/original.png", img)

gaussian = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imwrite("images/gaussian.png", gaussian)

median = cv2.medianBlur(img, 15)
cv2.imwrite("images/median.png", median)

kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpen = cv2.filter2D(img, -1, kernel)
cv2.imwrite("images/sharpen.png", sharpen)

laplacian = cv2.Laplacian(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
cv2.imwrite("images/laplacian.png", laplacian)

plt.figure(figsize=(4,3))
plt.imshow(cv2.cvtColor(gaussian, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("Gaussian Filter")
plt.tight_layout()
plt.savefig("images/gaussian_plot.png")
plt.close()

print("Semua gambar filter telah disimpan di folder 'images/'.")