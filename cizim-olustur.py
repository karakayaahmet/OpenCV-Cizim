import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8)
# canvas = np.zeros((512,512,3), dtype=np.uint8) + 100   Gri bir canvas
# canvas = np.zeros((512,512,3), dtype=np.uint8) + 255 Beyaz bir canvas

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
