#!/Users/darthnoward/anaconda3/bin/python
import cv2
import numpy as np

capture = cv2.VideoCapture(0)

kernel = np.ones((5,5),np.float32)/25

cv2.namedWindow('Video',cv2.WINDOW_NORMAL)

# cv2.namedWindow('Video1',cv2.WINDOW_NORMAL)


while capture.isOpened():
    ret, frame = capture.read()
    
    
    # Gradient (A high change in gradient indicates a major change in the image)
    # laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    # sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    
    
    # EDGE
    # edges = cv2.Canny(frame, 100, 200)
    
    cv2.resizeWindow('Video', 1200, 675)
    cv2.imshow('Video', sobelx)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break
capture.release()
cv2.destroyAllWindows()

