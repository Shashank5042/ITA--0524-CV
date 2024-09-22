import cv2

# Load the image
img = cv2.imread(r"C:\Users\deves\Downloads\CV IMAGES\images.jpeg", cv2.IMREAD_COLOR)

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load image.")
else:
    # Save the image to a file
    cv2.imwrite("output_image.jpeg", img)
    print("Image saved as 'output_image.jpeg'.")
