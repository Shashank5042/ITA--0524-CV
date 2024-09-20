import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Could not open or find the image.")
else:
    roberts_cross_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    roberts_cross_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    roberts_x = cv2.filter2D(image, -1, roberts_cross_x)
    roberts_y = cv2.filter2D(image, -1, roberts_cross_y)
    roberts_combined = np.sqrt(roberts_x ** 2 + roberts_y ** 2)
    roberts_combined = np.uint8(255 * roberts_combined / np.max(roberts_combined))
    plt.imshow(roberts_combined, cmap='gray')
    plt.title('Robert Edge Detection')
    plt.show()
