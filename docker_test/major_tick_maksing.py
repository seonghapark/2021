import cv2
import numpy as np
import glob
import argparse
import os
import datetime

def testrun(args):
    image = cv2.imread(args.test)
    print(len(image), len(image[0]))
    lower = np.array([255, 0, 255])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(image, lower, upper)

    cv2.imshow('frame', image)

    cv2.circle(mask, (240, 365), 210, (255, 255, 255), -1)
    res = cv2.bitwise_or(image, image, mask=mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(0) & 0xFF
    if k == ord('q'):
        return

def run(args):
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    path = args.indir + '*'
    files = sorted(glob.glob(path))
    dict_files = {}
    for i in files:
        num = int(i.strip().split('/')[-1].split('.')[0])
        dict_files[num] = i

    aa = dict_files[1].split('/')
    bb = args.outdir + aa[1]
    if not os.path.exists(bb):
        os.makedirs(bb)


    startdatetime = datetime.datetime.strptime(args.startdatetime, '%Y%m%d%H%M%S')
    for i in range(args.startnum, len(dict_files)):
        image = cv2.imread(dict_files[i])
        lower = np.array([255, 255, 255])
        upper = np.array([255, 255, 255])
        mask = cv2.inRange(image, lower, upper)

        cv2.imshow('frame', image)

        while True:
            cv2.circle(mask, (247, 316), 510, (0, 0, 0), -1)
            cv2.circle(mask, (247, 316), 212, (255, 255, 255), -1)
            cv2.rectangle(mask,(227,370),(269,273),(0,0,0),-1)
            cv2.rectangle(mask,(236,273),(252,100),(0,0,0),-1)

            pts = np.array([[254, 283], [254, 351], [426, 439], [457, 398]], np.int32)
            pts = pts.reshape((-1,1,2))

            cv2.polylines(mask, [pts], True, (0,0,0), 1)
            # cv2.fillPoly(mask, [pts], (0,0,0))

            res = cv2.bitwise_or(image, image, mask=mask)
            cv2.imshow('res',res)

            currentdatetime = startdatetime + datetime.timedelta(seconds=30*i)
            aa = dict_files[i+1].split('/')

            filename = args.outdir + aa[1] + '/' + \
                         datetime.datetime.strftime(currentdatetime, 'H%M%S') + '.jpg'
            print(filename)

            k = cv2.waitKey(0) & 0xFF
            if k == ord('a'):
                cv2.imwrite(filename, res)
                print(i, 'saved')
                break
            if k == ord('s'):
                break
            elif k == ord('q'):
                break
        if k == ord('q'):
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--indir', type=str, help='Input dir for images')
    parser.add_argument('--outdir', type=str, help='Output dir for images')
    parser.add_argument('--startdatetime', type=str)
    parser.add_argument('--startnum', type=int, default=1)
    parser.add_argument('--test', type=str)

    args = parser.parse_args()

    if args.test != None:
        testrun(args)
    else:
        if args.indir == None or args.outdir == None or \
            args.startdatetime == None:
            parser.print_help()
            exit(0)
        else:
            run(args)