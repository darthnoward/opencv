import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    fgmask = fgbg.apply(bw, learningRate = 0.1)
# apply (image, fgmask, learningRate = -1) method to get the foreground mask

    show=cv2.bitwise_and(frame,frame,mask=fgmask) 
    cv2.imshow('window',show)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break

cap.release()
cv2.destroyAllWindows()
