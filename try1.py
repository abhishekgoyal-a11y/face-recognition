import cv2
import numpy as np
img = cv2.imread('C:/Users/HP/Desktop/pythonopencvtut/videosandimage/dog.jpg')
edges = cv2.Canny(img, 200, 255)
# print(np.shape(edges)[0], np.shape(edges)[1])

print(np.asarray([100, 100]))
cv2.imshow("Edge Detected Image", edges)
cv2.imshow("Original Image", img)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()
