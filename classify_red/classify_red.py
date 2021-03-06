#!/Users/darthnoward/anaconda3/bin/python
import cv2
import numpy as np

capture = cv2.VideoCapture(0)

kernel = np.ones((5,5),np.float32)/25

cv2.namedWindow('Video',cv2.WINDOW_NORMAL)

cv2.namedWindow('Video1',cv2.WINDOW_NORMAL)


while capture.isOpened():
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_end = np.array([0,125,125])
    higher_end = np.array([5,255,255])
    
    mask = cv2.inRange(hsv, lower_end, higher_end)
    
    
    
    # smooth
    # smoothed = cv2.filter2D(res, -1, kernel)     
    
    
    # blur
    # blur = cv2.GaussianBlur(res,(5,5),0)
    # median = cv2.MedianBlur(res,5)
    # bilateral = cv2.bilateralFilter(res,15,75,75)
        
    # opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    
    # display frame where only where mask exists 
    res = cv2.bitwise_and(frame,frame, mask = closing)
    
    cv2.resizeWindow('Video', 800, 450)
    cv2.resizeWindow('Video1', 800, 450)
    cv2.imshow('Video',res)
    cv2.imshow('Video1',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break
capture.release()
cv2.destroyAllWindows()

