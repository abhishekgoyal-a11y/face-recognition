##import cv2
##import os
# face_classifier = cv2.CascadeClassifier(
# 'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
##
##cap = cv2.VideoCapture('birju.mp4')
##count = 0
##loop = True
# while loop:
##    ret, frame = cap.read()
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
# for (x, y, w, h) in faces:
# x1=w//2
# y1=h//2
# cv2.circle(frame,((x+x1),(y+y1)),x1,(0,255,0),1)
##    cv2.imshow("dsfs", frame)
##
# if cv2.waitKey(1) == 13 or count > 100:
##        loop = False
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# face_quality = cv2.CascadeClassifier(
#     'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# images = cv2.imread('group.jpg')
# faces = face_quality.detectMultiScale(images, 1.3, 1)
# for (x, y, w, h) in faces:
#     x1 = w//2
#     y1 = h//2
#     cv2.rectangle(images, (x, y), (x+w, y+h), (255, 0, 0), 1)
#     cv2.line(images, (x+w, y), (x+w+60, y-50), (255, 0, 0), 1)
#     cv2.line(images, (x+w, y), (x+w+60, y+h-80), (255, 0, 0), 1)
#     cv2.rectangle(images, (x+w+60, y-50), (x+w+140, y+h-80), (255, 0, 0), 1)

# print(faces)
# cv2.imshow("dfgd", images)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
face_quality = cv2.CascadeClassifier(
    'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
images = cv2.imread('group.jpg')
faces = face_quality.detectMultiScale(images, 1.3, 1)
for (x, y, w, h) in faces:
    x1 = w//2
    y1 = h//2
    cv2.line(images, (x, y), (x+x1-10, y), (0, 0, 255), 2)
    cv2.line(images, (x, y), (x, y+y1-10), (0, 0, 255), 2)

    cv2.line(images, (x, y+h), (x, y+y1+10), (0, 0, 255), 2)
    cv2.line(images, (x, y+h), (x+x1-10, y+h), (0, 0, 255), 2)

    cv2.line(images, (x+w, y+h), (x+w, y+y1+10), (0, 0, 255), 2)
    cv2.line(images, (x+w, y+h), (x+x1+10, y+h), (0, 0, 255), 2)

    cv2.line(images, (x+w, y), (x+x1+10, y), (0, 0, 255), 2)
    cv2.line(images, (x+w, y), (x+w, y+y1-10), (0, 0, 255), 2)

cv2.imshow("dfgd", images)
cv2.waitKey(0)
cv2.destroyAllWindows()


##import cv2
# face_quality = cv2.CascadeClassifier(
# 'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
##images = cv2.imread('dog1.jpg')
# alpha=0.3
##overlay = images.copy()
##output = images.copy()
##faces = face_quality.detectMultiScale(images, 1.3, 1)
##
# for (x, y, w, h) in faces:
# x1=w//2
# y1=h//2
# cv2.circle(overlay,((x+x1),(y+y1)),x1,(0,0,255),-1)
##    cv2.addWeighted(overlay, alpha, images, 1 - alpha,0, output)
##
##cv2.imshow("dfgd", output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# part2
##import cv2
# face_quality = cv2.CascadeClassifier(
# 'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
##smile_quality = cv2.CascadeClassifier('C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_smile.xml')
##eye_quality = cv2.CascadeClassifier('C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_eye.xml')
##images = cv2.imread('person.jpg')
##faces = face_quality.detectMultiScale(images, 1.3, 2)
##smiles = smile_quality.detectMultiScale(images, 1.3, 5)
##eyes = eye_quality.detectMultiScale(images, 1.3, 2)
##count = 0
# for (x, y, w, h) in faces:
##    cv2.putText(images, 'face', (x,y), cv2.FONT_HERSHEY_SIMPLEX ,1, (0, 255, 0), 1)
##    cv2.rectangle(images, (x, y), (x+w, y+h), (0, 255, 0), 1)
# for (x, y, w, h) in eyes:
# count+=1
##    cv2.putText(images, str(count), (x,y), cv2.FONT_HERSHEY_SIMPLEX ,1, (0,0, 255), 1)
##    cv2.rectangle(images, (x, y), (x+w, y+h), (0, 0, 255), 1)
# for (x, y, w, h) in smiles:
##    cv2.putText(images, 'smile', (x,y), cv2.FONT_HERSHEY_SIMPLEX ,1, (255,0, 0), 1)
##    cv2.rectangle(images, (x, y), (x+w, y+h), (255, 0, 0), 1)
##
##cv2.imshow("dfgd", images)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# part3
##import cv2
# face_quality = cv2.CascadeClassifier(
# 'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
##
##cap = cv2.VideoCapture(0)
##
# while(True):
##    ret, frame = cap.read()
##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##    faces = face_quality.detectMultiScale(gray, 1.3, 5)
# for (x, y, w, h) in faces:
##        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0, 255), 2)
# images=cv2.resize(frame,(1366,768))
# cv2.imshow('frame',images)
# if cv2.waitKey(1) & 0xFF == ord('q'):
# break
##
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# # mouse callback function
# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONUP:
#         cv2.circle(img,(x,y),100,(255,0,0),-1)
#         print(x,y)
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image',draw_circle)
# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()

# https://www.pyimagesearch.com/2016/03/07/transparent-overlays-with-opencv/
