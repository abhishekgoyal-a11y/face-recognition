import cv2
import numpy as np
img = cv2.imread("image1.jpg")

kernel_3X3 = np.ones((7, 7), dtype="uint8")/49
# filter2d is used for filtering the image
blureed = cv2.filter2D(img, -1, kernel_3X3)
cv2.imshow("dfg", blureed)

cv2.waitKey(0)
cv2.destroyAllWindows()
