import cv2
import numpy as np
img = cv2.imread("image1.jpg")
square = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(square, (50, 50), (250, 250), 255, 1)
cv2.imshow("dfg", square)
cv2.waitKey(0)
cv2.destroyAllWindows()
