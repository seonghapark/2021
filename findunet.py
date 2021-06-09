import glob
import argparse
import os
import math
import shutil


def run(args):
    if not os.path.exists(args.irmaskoutdir):
        os.makedirs(args.irmaskoutdir)
    if not os.path.exists(args.rgboutdir):
        os.makedirs(args.rgboutdir)

    irmaskpath = args.irmaskindir + '*'
    irmaskfiles = sorted(glob.glob(irmaskpath))

    rgbpath = args.rgbindir + '*'
    rgbfiles = sorted(glob.glob(rgbpath))

    rgbfileslist = []

    for j in range(len(rgbfiles)):
        aa = int(rgbfiles[j].strip().split('/')[-1].split('.')[0])
        rgbfileslist.append(aa)
    # print(rgbfileslist)

    yesnames = []
    for i in range(len(irmaskfiles)):
        aa = int(irmaskfiles[i].strip().split('/')[-1].split('.')[0])
        frac, whole = math.modf(aa/100)
        # print(round(frac*100, 2), whole)
        if round(frac*100) % 30 == 0 and aa >= args.starttime:
            if aa in rgbfileslist:
                yesnames.append(aa)
    # print(yesnames)

    date = rgbfiles[0].strip().split('/')[1].split('_')[-1]
    # print(date)
    for i in yesnames:
        irmaskname = args.irmaskindir + str(i) + '.jpg'
        rgbname = args.rgbindir + str(i) + '.jpg'

        iroutname = args.irmaskoutdir + date + '_' + str(i) + '.jpg'
        rgboutname = args.rgboutdir + date + '_' + str(i) + '.jpg'
        # print(iroutname, rgboutname)

        shutil.copy2(irmaskname, iroutname)
        shutil.copy2(rgbname, rgboutname)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--irmaskindir', type=str, help='Input dir for images')
    parser.add_argument('--irmaskoutdir', type=str, help='Output dir for images')
    parser.add_argument('--rgbindir', type=str, help='Input dir for images')
    parser.add_argument('--rgboutdir', type=str, help='Output dir for images')
    parser.add_argument('--starttime', type=int)

    args = parser.parse_args()

    if args.irmaskindir == None or args.irmaskoutdir == None or \
       args.rgbindir == None or args.rgboutdir == None:
        parser.print_help()
        exit(0)
    else:
        run(args)
