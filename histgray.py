
import cv2
import matplotlib.pyplot as plt
gray = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg', cv2.IMREAD_GRAYSCALE)
equalized = cv2.equalizeHist(gray)
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title('Original')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(equalized, cmap='gray')
plt.title('Equalized')
plt.axis('off')
plt.show()
