#!/Users/darthnoward/anaconda3/bin/python
import cv2
import numpy as np

cv2.namedWindow('window',cv2.WINDOW_NORMAL)

img = cv2.imread('keyboard.jpg',-1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread("key2.jpg",0)

height, width = template.shape[::-1]

result = cv2.matchTemplate(gray, template, cv2.TM_CCORR_NORMED)
loc = np.where(result >= 0.9) # get the location where it matches 


for pt in zip(*loc[::-1]):  # np.where return twp arrays representing width and height, however rectangle function (and so does all normal stuff) needs argument as (height, width), so a transformation is performed.
	cv2.rectangle(img, pt, (pt[0]+width,pt[1]+height), (0,0,255), 1)
	# draw a rectrangle where matches


cv2.imshow('window',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
