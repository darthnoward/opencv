import cv2
import numpy as np 


img = cv2.imread('1.jpg',-1)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# bigger than 150 then set to be 255

ret, mask_inv = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)
# bigger than 150 then set to be 255, then reverse
mask_inverse = cv2.bitwise_not(mask)
# bitwise_ is just like logical operator
# this mask is the white area 

# mask_inv[:,:] = 200
cv2.imshow("window", mask_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()
