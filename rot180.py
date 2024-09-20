
import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg')
rotated_180 = cv2.rotate(img, cv2.ROTATE_180)
plt.imshow(cv2.cvtColor(rotated_180, cv2.COLOR_BGR2RGB))
plt.title('180 Degrees Clockwise')
plt.axis('off')
plt.show()
