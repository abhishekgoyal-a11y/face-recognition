import cv2
# imread is used for reading the image
img = cv2.imread("image1.jpg")
# imshow is used for display the images
cv2.imshow('images', img)
# write is used for writting the image
cv2.imwrite('image1.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
