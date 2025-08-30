# face_recognition_project
This project uses Python, OpenCV, and the face_recognition library to detect and recognize faces in real-time using a webcam or images.

🚀 Features
Detect faces from images and webcam
Recognize known faces by comparing encodings
Store and organize face data in folders
Simple and beginner-friendly implementation  

🛠️ Technologies Used
Python 3.x
OpenCV (cv2)
face_recognition
NumPy

📂 Project Structure
FACE_RECOGNITION_PROJECT/
│-- FACES/                 # Folder to store known faces
│-- face_recognition.py    # Main Python script
│-- requirements.txt       # List of dependencies
│-- README.md              # Project documentation

🔧 Installation & Setup
Clone the repository:
git clone https://github.com/Bhoobesh1/face_recognition_project.git
cd face_recognition_project

Install dependencies:
pip install -r requirements.txt


Run the project:
python face_recognition.py


🎯 How It Works
Place known face images in the FACES/ folder (each person should have their own subfolder).
Run the script → the webcam will open.
The program detects faces and compares them with the stored encodings.
If a match is found, it displays the person’s name; otherwise, it shows "Unknown".

📸 Example Output
Known face detected → ✅ Shows the person’s name.
Unknown face → ❌ Displays "Unknown".

✨ Future Improvements
Improve accuracy with deep learning models
Add attendance system feature
Create a GUI interface
    
👤 Author
Bhoobesh
GitHub: Bhoobesh1
