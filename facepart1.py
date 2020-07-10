import cv2
import os
face_classifier = cv2.CascadeClassifier(
    'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is():
        return None
    for (x, y, w, h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    return cropped_face


cap = cv2.VideoCapture(0)
count = 0
loop = True
while loop:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (400, 400))
        file_name_path = 'C:/Users/HP/Desktop/image/user'+str(count)+".jpg"
        cv2.imwrite(file_name_path, face)
        cv2.putText(face, str(count), (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0))
        cv2.imshow("dsfs", face)
    else:
        print("face is not recognized")
    if cv2.waitKey(1) == 13 or count > 100:
        loop = False
cap.release()
cv2.destroyAllWindows()
