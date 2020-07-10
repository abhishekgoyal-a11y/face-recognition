import cv2
import os
import numpy as np
import tut
test_img = cv2.imread(
    'C:/Users/HP/Desktop/pythonopencvtut/videosandimage/person.jpg')
face_detected, grayimg = tut.facedetecton(test_img)
for (x, y, w, h) in face_detected:
    cv2.rectangle(test_img, (x, y), (x+w, y+h), (255, 0, 0), 1)
resizedimg = cv2.resize(test_img, (1000, 700))
cv2.imshow("Dfg", resizedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
