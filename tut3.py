import cv2
# imread is used for reading the image
img = cv2.imread("image1.jpg")
# imshow is used for display the images
cv2.imshow('images', img)
# shape is used for giving the detail of an image
print(img.shape)
# output is (height ,width , layer) layer we are using here is "rgb"

cv2.waitKey(0)
cv2.destroyAllWindows()
