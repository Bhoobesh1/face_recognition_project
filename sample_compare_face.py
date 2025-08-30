import cv2
import face_recognition

imgElon = face_recognition.load_image_file(r"C:\Users\bhoob\OneDrive\Documents\FACE_RECOGNITION_PROJECT\Elon Musk.png")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgElon = cv2.resize(imgElon, (600, 500))# work faster if the image size is small

imgBill = face_recognition.load_image_file(r"C:\Users\bhoob\OneDrive\Documents\FACE_RECOGNITION_PROJECT\Bill Gates.png")
imgBill = cv2.cvtColor(imgBill, cv2.COLOR_BGR2RGB)
imgBill = cv2.resize(imgBill, (600, 500)) # work faster if the image size is small


faceLoc = face_recognition.face_locations(imgElon)[0]  #face location (top,right ,bottom ,left)
encodeElon = face_recognition.face_encodings(imgElon,[faceLoc])[0] #128 dimentions
print(f"eleon musk: {encodeElon}")
print(type(encodeElon))
cv2.rectangle(imgElon, pt1=(faceLoc[3], faceLoc[0]), pt2=(faceLoc[1], faceLoc[2]), color=(0, 0, 255), thickness=2)

facelocBill = face_recognition.face_locations(imgBill)[0]
encodeBill = face_recognition.face_encodings(imgBill,[facelocBill])[0]
print(f"bill gates : {encodeBill}")
print(type(encodeBill))
cv2.rectangle(imgBill, pt1=(facelocBill[3], facelocBill[0]), pt2=(facelocBill[1], facelocBill[2]), color=(0, 0, 255), thickness=2)

results = face_recognition.compare_faces([encodeElon], encodeBill) # compare second face with list of first face    
# result = False means, not same person, result=True means, same person but the result will be in list format
facedis = face_recognition.face_distance([encodeElon], encodeBill)
print(results, facedis)
cv2.putText(imgBill, f"{results}, {facedis[0]:.2f}", (50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(255, 0, 255), 3)

cv2.imshow("ImageElon", imgElon)
cv2.imshow("ImageBill", imgBill)
cv2.waitKey(0)

"""
face_locations = [(100, 200, 180, 120), (50, 150, 120, 80)]
face_encodings = [array([0.1, 0.2, ..., 0.128]), array([0.2, 0.3, ..., 0.128])]
facedis => if (0.6> facedis => same person) (coloser to 0 => more accurate)

"""