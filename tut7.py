import cv2
import numpy as np
img = cv2.imread("thewizard.jpg")
cv2.imshow("img", img)
# split the color into rgb
B, G, R = cv2.split(img)
# here we are creating an zero array list
zero = np.zeros(img.shape[:2], dtype="uint8")
# here we are merging the color
cv2.imshow("red", cv2.merge([R, zero, B]))
cv2.waitKey(0)
cv2.destroyAllWindows()
