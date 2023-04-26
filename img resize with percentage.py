import cv2
import numpy as np

img = cv2.imread("sample.jpg")
# FOR KNOWLEDGE
# height = img.shape[0]
# width = img.shape[1]
# channels = img.shape[2]

img_resize = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2)) # REDUCING BOTH WIDTH AND HEIGHT BY 50%

print(img_resize.shape)  # SIZE OF RESIZED IMAGE FOR CONFIRMATION

cv2.imshow("window", img_resize)  # SHOW THE IMAGE
cv2.waitKey(0)  # SO THAT IT WAITS ON THE WINDOW
