import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread(r'/Users/chrisnikky/Downloads/helo.jpeg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Define Prewitt operator kernels
    prewitt_kernel_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
    prewitt_kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)

    # Apply the Prewitt operator using filter2D
    prewitt_x = cv2.filter2D(image, -1, prewitt_kernel_x)
    prewitt_y = cv2.filter2D(image, -1, prewitt_kernel_y)

    # Compute the gradient magnitude (edge intensity)
    prewitt_combined = np.sqrt(prewitt_x ** 2 + prewitt_y ** 2)

    # Normalize the result to display properly
    prewitt_combined = np.uint8(255 * prewitt_combined / np.max(prewitt_combined))

    # Display the results
    plt.imshow(prewitt_combined, cmap='gray')
    plt.title('Prewitt Edge Detection')
    plt.show()
