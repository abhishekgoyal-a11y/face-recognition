import cv2
import numpy as np
img = cv2.imread("image1.jpg")

height, width = img.shape[:2]

quarter_height, quarter_width = height/4, width/4
T = np.float32([[1, 0, quarter_height],
                [0, 1, quarter_width]])
# image displacement is happened
# warpaffine is used to change the x and y coordinates of image (image define ,how much want to shift,(width and height of image))
img_translation = cv2.warpAffine(img, T, (width, height))
cv2.imshow("asfs", img)
cv2.imshow("wrwet", img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
