from re import T
from ssl import PROTOCOL_SSLv23
import cv2
import numpy as np

canvas = np.zeros((512,512,3), np.uint8) + 255

# çizgi oluşturma
cv2.line(canvas,(50,50),(100,150),(255,0,0),thickness=5)
cv2.line(canvas,(20,20),(333,333),(0,0,255),thickness=4)

# dörtgen oluşturma
cv2.rectangle(canvas, (30,30),(150,150), (234,200,23), thickness=-1)  #thickness = -1 içi dolu.
cv2.rectangle(canvas, (50,60),(120,150), (123,23,42), thickness=-1)

# çember oluşturma
cv2.circle(canvas, (250,250), 100, (50,50,50), thickness=-1)

# üçgen çizimi
p1 = (200,200)
p2 = (400,400)
p3 = (20,20)

cv2.line(canvas, p1,p2, (0,0,0), thickness=3)
cv2.line(canvas, p2,p3, (0,0,0), thickness=4)
cv2.line(canvas, p1,p3, (0,0,0), thickness=5)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()