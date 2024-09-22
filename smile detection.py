import cv2
import matplotlib.pyplot as plt

# Load the pre-trained Haar Cascade classifiers for face and smile detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Check if the cascades are loaded properly
if face_cascade.empty() or smile_cascade.empty():
    print("Error loading cascade classifier")

# Load the image
image = cv2.imread(r"C:\Users\deves\Downloads\CV IMAGES\download (1).jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces and detect smiles within each face
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Region of interest for the face to detect the smile
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    # Detect smiles within the face region
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)

    # Draw rectangles around the detected smiles
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

# Convert the image from BGR to RGB for displaying with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the output using matplotlib
plt.imshow(image_rgb)
plt.axis('off')  # Hide the axes
plt.show()
