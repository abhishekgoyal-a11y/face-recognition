import cv2
import os
import numpy as np


def facedetecton(test_img):
    grayimg = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(
        'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    faces = face_classifier.detectMultiScale(
        grayimg, scaleFactor=1.32, minNeighbors=1)
    return grayimg, faces
