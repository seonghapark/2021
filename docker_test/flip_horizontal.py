import cv2
import glob
import argparse
import os
import datetime

def testrun(args):
    image = cv2.imread(args.test)
    cv2.imshow('frame', image)
    fliphorizontal = cv2.flip(image, 1)
    cv2.imshow('res',fliphorizontal)

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
    for i in range(len(dict_files)):
        image = cv2.imread(dict_files[i+1])
        # cv2.imshow('frame', image)

        fliphorizontal = cv2.flip(image, 1)
        # cv2.imshow('res',fliphorizontal)

        currentdatetime = startdatetime + datetime.timedelta(seconds=30*i)
        aa = dict_files[i+1].split('/')

        filename = args.outdir + aa[1] + '/' + \
                datetime.datetime.strftime(currentdatetime, '%H%M%S') + '.jpg'
        # print(filename)
        cv2.imwrite(filename, fliphorizontal)

        # k = cv2.waitKey(0) & 0xFF
        # if k == ord('q'):
        #     break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--indir', type=str, help='Input dir for images')
    parser.add_argument('--outdir', type=str, help='Output dir for images')
    parser.add_argument('--startdatetime', type=str)
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