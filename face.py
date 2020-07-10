import cv2
import numpy as np
import os


def facedetection(test_img):
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    face_haar_cascade = cv2.CascadeClassifier(
        'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    faces = face_haar_cascade.detectMultiScale(gray_img, 1.3, 5)
    return faces, gray_img


def labels_for_training_data(directory):
    faces = []
    faceID = []
    for path, subdirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filenames.startswith("."):
                print("sadsak")
                continue
        id=os.path.basename(path)
        img_path=os.path.join(path,filename)
        print("image_path",img_pth)
        print("id:",id)
        test_img = cv2.imread(img_path)
        if test_img is None:
            print("imaage is not loaded")
            continue
        faces_rect,gray_img=facedetection(test_img)
        if len(faces_rect)!=1:
            continue
        (x,y,w,h)=faces_rect[0]
        roi_gray=gray_img[y:y+w,x:x+h]
        faces.append(roi_gray)
        faceID.append(int(id))
    return faces,faceID


def train_classifier(faces, faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer
def draw_rect(test_img,face)
