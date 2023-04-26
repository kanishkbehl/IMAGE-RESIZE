import cv2
import numpy as np

img = cv2.imread("sample.jpg")
img_resize = cv2.resize(img,(256,256))

print(img_resize.shape)         #SIZE OF RESIZED IMAGE FOR CONFIRMATION

cv2.imshow("window",img_resize) #SHOW THE IMAGE
cv2.waitKey(0)                  #SO THAT IT WAITS ON THE WINDOW

