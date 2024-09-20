
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg')
roi = img[100:200, 100:200]  
img[50:150, 50:150] = roi  
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Modified ROI')
plt.axis('off')
plt.show()
