import cv2
import numpy as np
img = cv2.imread("image1.jpg")
height, width = img.shape[:2]
# rotating the image(image coordinates,angle rotation,scale of image)
rotation_angle = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
img_rotate = cv2.warpAffine(img, rotation_angle, (height, width))
cv2.imshow("image", img_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
