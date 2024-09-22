import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Check if the cascade is loaded properly
if face_cascade.empty():
    print("Error loading cascade classifier")

# Load the image
image = cv2.imread(r'C:\Users\deves\Downloads\CV IMAGES\download.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image (try adjusting scaleFactor and minNeighbors)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Check if faces are detected
if len(faces) == 0:
    print("No faces detected")
else:
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('Image with Detected Faces', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
