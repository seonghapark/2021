import sys
import numpy as np
import cv2
import glob
import os

def draw_circle(event,x,y,flags,param):
    global mouseX, mouseY, masking, unmasking
    if event == cv2.EVENT_MOUSEMOVE:
        if masking:
            cv2.circle(mask, (x, y), 5, (255, 255, 255), -1)
            res = cv2.bitwise_or(image, image, mask=mask)
            cv2.imshow('res',res)
        if unmasking:
            cv2.circle(mask, (x, y), 5, (0,0,0), -1)
            res = cv2.bitwise_or(image, image, mask=mask)
            cv2.imshow('res',res)
    # elif event == cv2.EVENT_LBUTTONDOWN:
    #     unmasking = True
    # elif event == cv2.EVENT_LBUTTONUP:
    #     unmasking = False
    # elif event == cv2.EVENT_RBUTTONDOWN:
    #     masking = True
    # elif event == cv2.EVENT_RBUTTONUP:
    #     masking = False


path = sys.argv[1]+'/*.jpg'
files = glob.glob(path)

print(len(files))
print('image: ', files[0].split('/')[-1])

image = cv2.imread(
    'data/sgptsiskycoverE42.b1.mask_noon_image.20170805.png')
height, width, channels = image.shape
print(image.shape)

masking = False
unmasking = False
lower = np.array([255, 0, 255])
upper = np.array([255, 255, 255])
mask = cv2.inRange(image, lower, upper)
cv2.imshow('frame',image)
cv2.setMouseCallback('frame', draw_circle)
while True  :
    cv2.imshow('frame', image)
    k = cv2.waitKey(20) & 0xFF
    if k == ord('q'):
        break
    elif k == ord('a'):
        masking = True
    elif k == ord('s'):
        masking = False
    elif k == ord('z'):
        unmasking = True
    elif k == ord('x'):
        unmasking = False
