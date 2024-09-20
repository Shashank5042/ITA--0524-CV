import cv2
import matplotlib.pyplot as plt

# Load the input image in grayscale
image = cv2.imread(r"/Users/chrisnikky/Downloads/helo.jpeg", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Apply Binary Thresholding
    # cv2.threshold() returns two values: the computed threshold and the binary image
    # 127 is the threshold value, 255 is the maximum value to use with THRESH_BINARY
    # You can adjust the threshold value as needed
    threshold_value = 127
    max_value = 255
    _, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

    # Display the original image and the binary image
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Grayscale Image')

    plt.subplot(1, 2, 2)
    plt.imshow(binary_image, cmap='gray')
    plt.title('Binary Thresholding')

    plt.show()
