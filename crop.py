import cv2

# Step 1: Load the source image
image = cv2.imread(r"/Users/chrisnikky/Downloads/helo.jpeg")

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Step 2: Define the Region of Interest (ROI)
    # ROI coordinates (x1, y1) -> top-left corner and (x2, y2) -> bottom-right corner
    x1, y1 = 100, 100  # Top-left corner of the ROI
    x2, y2 = 300, 300  # Bottom-right corner of the ROI

    # Step 3: Crop the ROI from the image
    roi = image[y1:y2, x1:x2]  # Crop the image using NumPy slicing

    # Get the dimensions of the ROI
    roi_height, roi_width, _ = roi.shape

    # Step 4: Paste the cropped ROI onto a different position in the same image
    # Define new coordinates where the ROI will be pasted
    x_new, y_new = 400, 400

    # Ensure the new position in the image is large enough to hold the ROI
    if y_new + roi_height <= image.shape[0] and x_new + roi_width <= image.shape[1]:
        image[y_new:y_new + roi_height, x_new:x_new + roi_width] = roi
    else:
        print("Error: The ROI cannot fit at the new position.")

    # Step 5: Display the result
    cv2.imshow('Original Image with ROI Pasted', image)
    cv2.imshow('Cropped ROI', roi)  # Display the cropped ROI separately

    # Save the output image if needed
    cv2.imwrite(r"C:\Users\Madhavan Dodda\OneDrive\Documents\Pictures\ganesha-hindu-god-goddess-wallpaper-preview.jpg", image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
