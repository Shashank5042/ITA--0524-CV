import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image in grayscale
image = cv2.imread(r"/Users/chrisnikky/Downloads/helo.jpeg", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not open or find the image.")
else:
    
    binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 11, 2)

    # Display the original image and the binary image
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(binary_image, cmap='gray')
    plt.title('Adaptive Thresholding')

    plt.show()
