import cv2
import glob
import argparse
import os

def testrun(args):
    image = cv2.imread(args.test)
    cv2.imshow('frame', image)
    # crop_img = image[y:y+h, x:x+w]
    crop_img = image[99:534, 16:451]
    cv2.imshow('res',crop_img)

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
        # cv2.imshow('frame', image)

        crop_img = image[99:534, 16:451]
        # cv2.imshow('res',crop_img)

        currentdatetime = files[i].split('/')[-1]
        aa = args.indir.split('/')

        filename = args.outdir + aa[1] + '/' + currentdatetime
        # print(filename)

        cv2.imwrite(filename, crop_img)

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
