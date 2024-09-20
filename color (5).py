import cv2
img = cv2.imread("/Users/chrisnikky/Downloads/helo.jpeg", cv2.IMREAD_COLOR)
if img is None:
    print("Error: Could not load image.")
else:
    cv2.imshow("image", img) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
