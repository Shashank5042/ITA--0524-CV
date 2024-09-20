import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg')
smaller = cv2.resize(img, (200, 200))
larger = cv2.resize(img, (800, 800))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB))
plt.title('Smaller')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(larger, cv2.COLOR_BGR2RGB))
plt.title('Larger')
plt.axis('off')
plt.show()
