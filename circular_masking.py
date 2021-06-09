import cv2
import glob
import argparse
import os

def testrun(args):
    image = cv2.imread(args.test)
    
    lower = np.array([255, 0, 255])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(image, lower, upper)

    cv2.imshow('frame', image)

    cv2.circle(mask, (240, 316), 510, (0, 0, 0), -1)
    cv2.circle(mask, (233, 316), 218, (255, 255, 255), -1)
    # cv2.rectangle(mask,(227,370),(269,273),(0,0,0), 1)
    # cv2.rectangle(mask,(236,273),(252,100),(0,0,0), 1)
    res = cv2.bitwise_or(image, image, mask=mask)
    cv2.imshow('res',res)

    # (h, w) = image.shape[:2]
    # (cX, cY) = (w // 2, h // 2)
    # M = cv2.getRotationMatrix2D((cX, cY), -5, 1.0)
    # rotated = cv2.warpAffine(res, M, (w, h))
    # cv2.imshow('rotated', rotated)

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
        lower = np.array([255, 255, 255])
        upper = np.array([255, 255, 255])
        mask = cv2.inRange(image, lower, upper)

        # cv2.imshow('frame', image)

        cv2.circle(mask, (240, 316), 510, (0, 0, 0), -1)
        cv2.circle(mask, (233, 316), 218, (255, 255, 255), -1)
        # cv2.rectangle(mask,(227,370),(269,273),(0,0,0),-1)
        # cv2.rectangle(mask,(236,273),(252,100),(0,0,0),-1)
        res = cv2.bitwise_or(image, image, mask=mask)
        # cv2.imshow('res',res)

        currentdatetime = files[i].split('/')[-1]
        aa = files[i].split('/')
        filename = args.outdir + aa[1] + '/' + currentdatetime
        # print(filename)
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