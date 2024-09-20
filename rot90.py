import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg')
rotated_90 = cv2.transpose(img)
rotated_90 = cv2.flip(rotated_90, flipCode=1)  
plt.imshow(cv2.cvtColor(rotated_90, cv2.COLOR_BGR2RGB))
plt.title('90 Degrees Clockwise')
plt.axis('off')
plt.show()
