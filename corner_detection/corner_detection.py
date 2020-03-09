import cv2
import numpy as np 

img = cv2.imread("image/corners.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
# Input 8-bit or floating-point 32-bit, single-channel image

# parameters: image, maxCorners, qualityLevel, minDistance 
corners = cv2.goodFeaturesToTrack(gray, 50 ,0.01, 10)
# the smaller qualityLevel, the more resource spent
corners = np.int0(corners)


for each_corner in corners:
    x,y = each_corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)


cv2.imshow('window',img)
cv2.waitKey(0)
