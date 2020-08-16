import cv2
from os import listdir
from os.path import isfile, join
import numpy as np

data_path = 'C:/Users/HP/Desktop/image/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
Training_Data, Labels = [], []
for i, files in enumerate(onlyfiles):
    image_path = data_path+onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
    print(i)
Labels = np.asarray(Labels, dtype=np.int32)
# pip install opencv-contrib-python(for lbphfacerecognizer)
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("training data is completed")
face_classifier = cv2.CascadeClassifier(
    'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 6)
    if faces is():
        return img, []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


cap = cv2.VideoCapture(0)
loop = True
while loop:
    ret, frame = cap.read()
    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)
        if result[1] < 500:
            cofidence = int((1-(result[1])/300)*100)
            display_string = str(onlyfiles[0])
        cv2.putText(image, display_string, (100, 120),
                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
        if cofidence > 75:
            cv2.putText(image, "face is found", (100, 450),
                        cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)
            cv2.imshow("face", image)
        else:
            cv2.putText(image, "face is not found", (100, 450),
                        cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)
            cv2.imshow("face", image)
    except:
        cv2.putText(image, "face is not recognized", (100, 450),
                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)
        cv2.imshow("face", image)
        pass
    if cv2.waitKey(1) == 13:
        loop = False
cap.release()
cv2.destroyAllWindows()
