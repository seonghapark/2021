import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 10, (0, 0, 0), -1)
        mouseX, mouseY = x, y
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while True  :
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == ord('q'):
        break
    elif k == ord('a'):

        print(mouseX, mouseY)
cv2.destroyAllWindows()
