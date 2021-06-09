import sys
import numpy as np
import cv2
import glob
import os
path = sys.argv[1]+'/*.jpg'
#files = glob.glob('/home/sager/repos/dataset/cloud/sunspot/images_02-11-2020/*.jpg')
files = glob.glob(path)
fcount = 0
print('start number of photo?')
input_start = input()
if input_start == '':
    fcount = 0
else:
    fcount = int(input_start)
while True:
    print('image: ', files[fcount].split('/')[-1])
    image = cv2.imread(files[fcount])
    height, width, channels = image.shape
    print(image.shape)
    image = cv2.resize(image, (int(width/4), int(height/4)))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #th = int(input('Put value'))
    #lower = np.array([0, th, 0])
    #upper = np.array([255, 255, 255])
    def op_hsv(image, hsv, saturation):
        lower = np.array([0, 0, 0])
        upper = np.array([255, saturation, 255])
        mask = cv2.inRange(hsv, lower, upper)
        return mask
        #return cv2.bitwise_and(image, image, mask=mask)
    def op_rgb(image, red=255, blue=255):
        lower = np.array([blue, 0, red])
        upper = np.array([255, 255, 255])
        mask = cv2.inRange(image, lower, upper)
        return mask
        #return cv2.bitwise_and(image, image, mask=mask)
    saturation = 0
    value = 0
    red = 0
    blue = 0
    while True:
        hsv_mask = op_hsv(image, hsv, saturation)
        rgb_mask = op_rgb(image, red, blue)
        #hsv_mask = cv2.bitwise_or(hsv_mask, hsv_mask, mask=rgb_mask)
        mask = cv2.bitwise_or(hsv_mask, hsv_mask, mask=rgb_mask)
        res = cv2.bitwise_or(image, image, mask=mask)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        cv2.imshow('frame',image)
        k = cv2.waitKey(0) & 0xFF
        if k == ord('y'):
            saturation += 2
            if saturation > 255:
                saturation = 255
        elif k == ord('h'):
            saturation -= 2
            if saturation < 0:
                saturation = 0
        elif k == ord('t'):
            value += 2
            if value > 255:
                value = 255
        elif k == ord('g'):
            value -= 2
            if value < 0:
                value = 0
        elif k == ord('u'):
            red += 2
            if red > 255:
                red = 255
        elif k == ord('j'):
            red -= 2
            if red < 0:
                red = 0
        elif k == ord('i'):
            blue += 2
            if blue > 255:
                blue = 255
        elif k == ord('k'):
            blue -= 2
            if blue < 0:
                blue = 0
        elif k == ord('q'):
            break
        print('saturation: {0}\t red: {1}\t blue: {2}'.format(saturation, red, blue))
    cv2.destroyAllWindows()
    masking = False
    unmasking = False
    def draw_circle(event,x,y,flags,param):
        global mouseX, mouseY, masking, unmasking
        if event == cv2.EVENT_MOUSEMOVE:
            if masking:
                cv2.circle(mask, (x, y), 5, (255, 255, 255), -1)
                res = cv2.bitwise_or(image, image, mask=mask)
                cv2.imshow('res',res)
            elif unmasking:
                cv2.circle(mask, (x, y), 5, (0,0,0), -1)
                res = cv2.bitwise_or(image, image, mask=mask)
                cv2.imshow('res',res)
        elif event == cv2.EVENT_LBUTTONDOWN:
            unmasking = True
        elif event == cv2.EVENT_LBUTTONUP:
            unmasking = False
        elif event == cv2.EVENT_RBUTTONDOWN:
            masking = True
        elif event == cv2.EVENT_RBUTTONUP:
            masking = False
    cv2.imshow('res',res)
    cv2.imshow('frame',image)
    cv2.namedWindow('mask')
    cv2.setMouseCallback('mask', draw_circle)
    while True  :
        cv2.imshow('mask', mask)
        k = cv2.waitKey(20) & 0xFF
        if k == ord('q'):
            break
    cv2.destroyAllWindows()
    print('save the mask? y or n')
    input_save = input()
    if input_save == 'y':
        test = files[fcount].split('/')
        test[-2] = 'gt_' + test[-2]
        test[-1] = 'gt_' + test[-1]
        s = '/'
        s = s.join(test)
        gt = '/'
        gt = gt.join(test[:-1])
        #print(gt)
        print(s)
        if not os.path.exists(gt):
            print('create gt folder')
            os.makedirs(gt)
        mask = cv2.resize(mask, (width, height))
        cv2.imwrite(s, mask)
    print('will do next photo? y or n')
    input_next = input()
    if input_next == 'n':
        print(fcount)
        break;
    else:
        print(fcount)
        fcount += 1
2:52
sager@sager-W65-67SC:~/repos/annotation_methods$ cat circle_on_image.py 
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
