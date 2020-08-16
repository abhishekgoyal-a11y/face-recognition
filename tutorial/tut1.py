import cv2
# imread is used for reading the image
img = cv2.imread("thewizard.jpg")
# imshow is used for display the images
cv2.imshow('images', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
