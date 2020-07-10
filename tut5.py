import cv2
img = cv2.imread("thewizard.jpg")
cv2.imshow("dsfds", img)
# converting image to threshold binary image
# (127,255)=(below or equal to 127 is black color and between 127 to 255 is white color)
ret, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("dsfdsf", bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
