import cv2
# second method use "0" for converting the images
img = cv2.imread("image1.jpg", 0)
cv2.imshow('images', img)
# converting rgb to gray color image(first method)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
