import cv2
import glob
import argparse
import os

def testrun(args):
    image = cv2.imread(args.test)
    cv2.imshow('frame', image)
    # cv2.ellipse(image, center_coordinates, axesLength, angle, \
    #             startAngle, endAngle, color, thickness)
    ellipse = cv2.ellipse(image, (332, 11), (30, 15), 5, \
                          0, 360, (0,0,0), -1)
    cv2.imshow('res',ellipse)

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

        ellipse = cv2.ellipse(image, (332, 11), (30, 15), 5, \
                      0, 360, (0,0,0), -1)
        # cv2.imshow('res',ellipse)


        filename = args.outdir +aa[1] + \
                    '/'+ files[i].split('/')[-1]
        # print(filename)
        cv2.imwrite(filename, ellipse)

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

