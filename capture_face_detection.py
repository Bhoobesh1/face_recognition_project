import cv2
import os
import time
name = input("enter the name of the person")

# Create directory to store face images
folder = r"C:\Users\bhoob\OneDrive\Documents\FACE_RECOGNITION_PROJECT\FACES"
folder_path=os.path.join(folder,name)
os.makedirs(folder_path, exist_ok=True) # Create folder if it doesn't exist if, it exists it will not give error

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Start webcam
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame,1) # flip the frame horizontally
    if not ret:
        break
    
    faces = face_cascade.detectMultiScale(frame, 1.1, 5)

    for (x, y, w, h) in faces: #(x is top left corner x coordinate, y is top left corner y coordinate, w is width of rectangle, h is height of rectangle)
        roi = frame[y:y+h, x:x+w]  # region of intrest, it gives face area only which slices the image into rows and columns
        #rows is slices in vertical direction
        #columns is slices in horizontal direction
        count += 1 
        time.sleep(0.5)
        file_path = os.path.join(folder_path, f"{name}{count}.jpg")
        cv2.imwrite(file_path, roi)
        cv2.putText(frame, f"Saved: {count}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Capturing Face Images", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 20:
        break

cap.release()
cv2.destroyAllWindows()

"""
folder = f"faces/{name}"
os.makedirs(folder, exist_ok=True)
python code checks faces folder is created or not
if not created it will create faces folder only once   

exist_ok=True makes sure no error happens if the folder already exists.

-------------------------------------------------------------------------
detectMultiScale()
This is the function that finds objects (faces) in the image.

1.1 (scaleFactor)
Specifies how much the image size is reduced at each scale.
1.1 means scale down by 10% per step.
Smaller = more accurate but slower.

5 (minNeighbors)
How many neighbors each candidate rectangle should have to retain it.
Higher = fewer detections (more strict).
Lower = more detections (less strict, more false positives).

roi = frame[y:y+h, x:x+w]
This line is used to focus only on the face region inside the full image (frame).


"""
