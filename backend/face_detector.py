import cv2

# Load the image
img = cv2.imread('example3.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the Haar Cascade face detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Loop through each face and extract the face image
for (x, y, w, h) in faces:
    # Create a bounding box around the face
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Extract the face image from the original image
    face_img = img[y:y+h, x:x+w]
    
    # Display the face image
    cv2.imshow('Face', face_img)
    cv2.waitKey(0)
    
# Display the original image with the bounding boxes around the faces
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()