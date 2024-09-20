import cv2
import matplotlib.pyplot as plt
img = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg')
rotated_270 = cv2.transpose(img)
rotated_270 = cv2.flip(rotated_270, flipCode=0)  # Flip vertically
plt.imshow(cv2.cvtColor(rotated_270, cv2.COLOR_BGR2RGB))
plt.title('270 Degrees Clockwise')
plt.axis('off')
plt.show()
