import cv2
import numpy as np
img = cv2.imread("image1.jpg")
# resize to half of image
smaller = cv2.pyrDown(img)
# resize to double of image
larger = cv2.pyrUp(img)

cv2.imshow("image", smaller)
cv2.imshow("image1", larger)
cv2.waitKey(0)
cv2.destroyAllWindows()
