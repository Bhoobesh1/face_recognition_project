import cv2

# Load the face cascade
cascade_path=cv2.data.haarcascades+"haarcascade_frontalface_default.xml" #path to the haarcascade file
face_cascade = cv2.CascadeClassifier(cascade_path)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale (face detection works better and increases performance)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
 
        print(x,y,w,h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (0, 255, 0), -1)
        cv2.putText(frame, "Bhoobesh", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        # if y increases then the text goes down 
        # if y decreases then the text goes up

    # Show the result
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) in [ord('q'),ord('Q')]:
        break

cap.release()
cv2.destroyAllWindows()

'''
            ↑
            |
            | y (decreases upward)
            |
(0,0) ------+--------------------------→ x (increases right)
            |
            | y (increases downward)
            |

'''