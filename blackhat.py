import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the input image in grayscale
image = cv2.imread(r"/Users/chrisnikky/Downloads/helo.jpeg", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Define the structuring element for the closing operation
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))  # You can use other shapes like cv2.MORPH_RECT or cv2.MORPH_CROSS

    # Apply the closing operation
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # Compute the Black-Hat transform
    black_hat = cv2.subtract(closing, image)

    # Display the original image, closed image, and Black-Hat result
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(closing, cmap='gray')
    plt.title('Closing Operation')

    plt.subplot(1, 3, 3)
    plt.imshow(black_hat, cmap='gray')
    plt.title('Black-Hat Transform')

    plt.show()
