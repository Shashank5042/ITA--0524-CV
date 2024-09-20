
import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg')
rows, cols, _ = img.shape
M = np.float32([[1, 0, 50], [0, 1, 100]]) 
translated = cv2.warpAffine(img, M, (cols, rows))
plt.imshow(cv2.cvtColor(translated, cv2.COLOR_BGR2RGB))
plt.title('Translated Image')
plt.axis('off')
plt.show()
