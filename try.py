import cv2
import os
eye_classifier = cv2.CascadeClassifier(
    'C:/Users/HP/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)
loop = True
while loop:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = eye_classifier.detectMultiScale(gray, 1.3, 5)
    p = 237
    q = 156
    r = 200
    s = 200
    t = r//2
    u = s//2
    if faces is not None:
        cv2.line(frame, (p, q), (p+t-10, q), (0, 255, 0), 2)
        cv2.line(frame, (p, q), (p, q+u-10), (0, 255, 0), 2)

        cv2.line(frame, (p, q+s), (p, q+u+10), (0, 255, 0), 2)
        cv2.line(frame, (p, q+s), (p+t-10, q+s), (0, 255, 0), 2)

        cv2.line(frame, (p+r, q+s), (p+r, q+u+10), (0, 255, 0), 2)
        cv2.line(frame, (p+r, q+s), (p+t+10, q+s), (0, 255, 0), 2)

        cv2.line(frame, (p+r, q), (p+t+10, q), (0, 255, 0), 2)
        cv2.line(frame, (p+r, q), (p+r, q+u-10), (0, 255, 0), 2)
    else:
        for (x, y, w, h) in faces:
            cv2.line(frame, (p, q), (p+t-10, q), (0, 0, 255), 2)
            cv2.line(frame, (p, q), (p, q+u-10), (0, 0, 255), 2)

            cv2.line(frame, (p, q+s), (p, q+u+10), (0, 0, 255), 2)
            cv2.line(frame, (p, q+s), (p+t-10, q+s), (0, 0, 255), 2)

            cv2.line(frame, (p+r, q+s), (p+r, q+u+10), (0, 0, 255), 2)
            cv2.line(frame, (p+r, q+s), (p+t+10, q+s), (0, 0, 255), 2)

            cv2.line(frame, (p+r, q), (p+t+10, q), (0, 0, 255), 2)
            cv2.line(frame, (p+r, q), (p+r, q+u-10), (0, 0, 255), 2)
    cv2.imshow("dsfs", frame)
    if cv2.waitKey(1) == 13:
        loop = False
cap.release()
cv2.destroyAllWindows()
