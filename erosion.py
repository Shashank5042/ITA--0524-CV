
import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(img, kernel, iterations=1)
plt.imshow(eroded, cmap='gray')
plt.title('Erosion')
plt.axis('off')
plt.show()
