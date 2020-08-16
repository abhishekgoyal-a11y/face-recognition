import cv2
import numpy as np
img = cv2.imread("image1.jpg")
M = np.ones(img.shape, dtype="uint8")*150
add = cv2.add(img, M)
subtract = cv2.subtract(img, M)
multiply = cv2.multiply(img, M)
division = cv2.divide(img, M)
cv2.imshow("im", subtract)
cv2.waitKey(0)
cv2.destroyAllWindows()
