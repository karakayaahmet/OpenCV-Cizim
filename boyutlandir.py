import cv2 
import numpy as np

canvas = np.zeros((10,10,3), np.uint8)
cv2.imshow("Canvas", canvas)

img = cv2.resize(canvas,(1000,1000), interpolation=cv2.INTER_AREA)

# canvas[0,0] = (255,255,255)
# canvas[0,1] = (255,255,200)
# canvas[0,2] = (255,255,150)
# canvas[0,3] = (255,255,15)
 
cv2.imshow("İmage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()