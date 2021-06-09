import cv2
import numpy as np
import glob
import argparse
import os
import datetime

def testrun(args):
    image = cv2.imread(args.test)
    image = cv2.resize(image, (423, 423), interpolation = cv2.INTER_AREA)

    lower = np.array([255, 255, 255])
    upper = np.array([0, 0, 0])
    mask = cv2.inRange(image, lower, upper)

    cv2.imshow('frame', image)

    cv2.circle(mask, (211, 211), 212, (255, 255, 255), -1)

    cv2.rectangle(mask,(206,0),(222,169),(0,0,0),-1)
    cv2.rectangle(mask,(189,168),(231,265),(0,0,0),-1)
        
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

    aa = files[1].split('/')
    bb = args.outdir + aa[1]
    if not os.path.exists(bb):
        os.makedirs(bb)

    for i in range(len(files)):
        image = cv2.imread(files[i])
        image = cv2.resize(image, (423, 423), interpolation = cv2.INTER_AREA)

        lower = np.array([255, 255, 255])
        upper = np.array([0, 0, 0])
        mask = cv2.inRange(image, lower, upper)
        # cv2.imshow('frame', image)

        cv2.circle(mask, (211, 211), 212, (255, 255, 255), -1)
        cv2.rectangle(mask,(206,0),(222,169),(0,0,0),-1)
        cv2.rectangle(mask,(189,168),(231,265),(0,0,0),-1)
            
        res = cv2.bitwise_or(image, image, mask=mask)
        # cv2.imshow('res',res)

        currentdatetime = files[i].split('/')[-1].split('.')[0]
        aa = args.indir.split('/')

        filename = args.outdir + aa[1] + '/' + currentdatetime + '.jpg'
        cv2.imwrite(filename, res)

        # k = cv2.waitKey(0) & 0xFF
        # if k == ord('q'):
        #     break



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--indir', type=str, help='Input dir for images')
    parser.add_argument('--outdir', type=str, help='Output dir for images')
    parser.add_argument('--test', type=str)

    args = parser.parse_args()

    if args.test != None:
        testrun(args)
    else:
        if args.indir == None or args.outdir == None:
            parser.print_help()
            exit(0)
        else:
            run(args)