import cv2
import numpy as np
import os
import face as fr
test_img = cv2.imread("image.jpg")
face_detected, gray_img = fr.facedetection(test_img)
for (x, y, w, h) in face_detected:
    cv2.rectangle(test_img, (x, y), (x+w, y+h), (0, 255, 0), 3, 2)
test_im = cv2.resize(test_img, (400, 400))
cv2.imshow("test image", test_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
