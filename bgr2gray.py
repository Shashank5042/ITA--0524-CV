import cv2
import matplotlib.pyplot as plt
img = cv2.imread('/Users/chrisnikky/Downloads/helo.jpeg') 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')  
plt.show()
