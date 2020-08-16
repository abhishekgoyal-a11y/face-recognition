import cv2
import numpy as np
img = cv2.imread("image1.jpg")
# (image,none,how much you want to resize it )
# showing the 3/4 of its original image
image_scale = cv2.resize(img, None, fx=0.75, fy=0.75)
# double the size of image
image_scale1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# exact dimension of image
image_scale2 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_AREA)


cv2.imshow("image", image_scale2)
cv2.waitKey(0)
cv2.destroyAllWindows()
