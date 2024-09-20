import cv2
import numpy as np

# Load the original image
image = cv2.imread(r"/Users/chrisnikky/Downloads/helo.jpeg")

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Create a watermark image (for this example, I'll use text as the watermark)
    watermark_text = "Sample Watermark"

    # Set font, scale, color, and thickness for the watermark text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 3
    color = (255, 255, 255)  # White color
    thickness = 5
    text_size = cv2.getTextSize(watermark_text, font, font_scale, thickness)[0]

    # Position the watermark text at the bottom-right corner of the image
    text_x = image.shape[1] - text_size[0] - 10  # 10 pixels from the right
    text_y = image.shape[0] - 10  # 10 pixels from the bottom

    # Create an overlay image for transparency
    overlay = image.copy()

    # Add the watermark text to the overlay image
    cv2.putText(overlay, watermark_text, (text_x, text_y), font, font_scale, color, thickness)

    # Blend the overlay with the original image using transparency
    alpha = 0.5  # Transparency factor (0.0 - fully transparent, 1.0 - fully opaque)
    watermarked_image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

    # Display the original and watermarked image
    cv2.imshow('Original Image', image)
    cv2.imshow('Watermarked Image', watermarked_image)

    # Save the result
    cv2.imwrite(r'C:\path\to\save\watermarked_image.jpg', watermarked_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
