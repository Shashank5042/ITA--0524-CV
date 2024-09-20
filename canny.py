import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread(r"/Users/chrisnikky/Downloads/helo.jpeg", cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Apply Canny edge detection
    edges = cv2.Canny(image, 100, 200)  # 100 and 200 are the lower and upper thresholds for edge detection

    # Display the original image and the edge-detected result
    plt.figure(figsize=(10,5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny Edge Detection')

    plt.show()
