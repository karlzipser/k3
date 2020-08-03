from k3.vis3 import *

import argparse





par = argparse.ArgumentParser(
    prog='mi',
    description='use mi from command line',
    fromfile_prefix_chars='@',
    add_help=True,
); aa = par.add_argument

aa(
    '-f',
    '--files',
    nargs="+",
    default=[],
    help='space-separated list of image files to show',
)

aa(
    '-p',
    '--paths',
    nargs="+",
    default=[],
    help='space-separated list of paths',
)

aa(
    '-r',
    '--raw_enter',
    action='store',
    type=int,
    required=False,
    default=1, 
    help='raw_enter option, 0 or 1',
)

aa(
    '-m',
    '--random',
    nargs='?',
    const=True, default=False,
    help="one image at a time",
)

aa(
    '--mwidth',
    action='store',
    type=int,
    required=False,
    default=400, 
    help='max width',
)

aa(
    '--mheight',
    action='store',
    type=int,
    required=False,
    default=400, 
    help='max height',
)

aa(
    "-o",
    "--one",
    nargs='?',
    const=True, default=False,
    help="one image at a time")

aa(
    "-d",
    "--descend",
    nargs='?',
    const=True, default=False,
    help="descend directories collecting images")




args = par.parse_args()

print(args)



try:
    os.system('mkdir -p '+opjh('Logs'))
    f = most_recent_file_in_folder(opjh('Logs'),str_elements=[fname(__file__)])
    L = lo(f)
except:
    L = {'full_paths':{},'filenames':{}}




lst = []

lst += args.files


import imghdr
lst0 = []
for p in args.paths:
    if args.descend:
        lst0 += get_list_of_files_recursively(p,'*',FILES_ONLY=True,ignore_underscore=False)
    else:
        lst0 += sggo(p,'*')



for l in lst0:
    try:
        if imghdr.what(l) is not None:
            lst.append(l)
    except:
        pass
if args.random:
    random.shuffle(lst)

kprint(lst,t='lst',r=0)


if using_osx:
    def screen_size():
        from Quartz import CGDisplayBounds
        from Quartz import CGMainDisplayID
        mainMonitor = CGDisplayBounds(CGMainDisplayID())
        return (mainMonitor.size.width, mainMonitor.size.height) 
    screen_sz = screen_size()
else:
    screen_sz = (800,800)

max_width,max_height = screen_sz[0]*0.9,screen_sz[1]*0.9
min_width,min_height = min(max_width,args.mwidth),min(max_height,args.mheight)

g = zeros((intr(max_height*1.),intr(max_width*1.),3),np.uint8)

for p in lst:
    img0, exif_for_image = load_image_with_orientation(p)
    img = get_resized_img(img0,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
    f = fname(p)
    if exif_for_image:
        c = '`y'
    else:
        c = '`'
    part1 = cf(fname(p),'`',pname(p),'`--du')
    if shape(img0) == shape(img):
        part2 = cf(shape(img0)[:2],c)
    else:
        part2 = cf(shape(img0)[:2],c,'-->',shape(img)[:2],'`r-b')
    clp(part1,part2)

    g *= 0
    img = place_img_f_in_img_g(0,0,img,g,f_center=True,center_in_g=True)
    cv2.namedWindow(f)
    cv2.moveWindow(f,int((screen_sz[0]-max_width)/2),0)

    k = mci(img,title=f)

    if args.one:
        e = getch()
        if p not in L:
            L['full_paths'][p] = []
        L['full_paths'][p].append((e,time.time()))

        CA()
        if e in ['q','Q','quit','exit']:
            sys.exit()

if not args.one and args.raw_enter:
    raw_enter()
so(L,opjh('Logs',fname(__file__)+'.'+str(int(time.time()))+'.log'))





import exifread
from PIL import Image

def _read_img_and_correct_exif_orientation(path):
    im = Image.open(path)
    tags = {}
    with open(path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    if "Image Orientation" in tags.keys():
        orientation = tags["Image Orientation"]
        logging.debug("Orientation: %s (%s)", orientation, orientation.values)
        val = orientation.values
        if 5 in val:
            val += [4,8]
        if 7 in val:
            val += [4, 6]
        if 3 in val:
            logging.debug("Rotating by 180 degrees.")
            im = im.transpose(Image.ROTATE_180)
        if 4 in val:
            logging.debug("Mirroring horizontally.")
            im = im.transpose(Image.FLIP_TOP_BOTTOM)
        if 6 in val:
            logging.debug("Rotating by 270 degrees.")
            im = im.transpose(Image.ROTATE_270)
        if 8 in val:
            logging.debug("Rotating by 90 degrees.")
            im = im.transpose(Image.ROTATE_90)

    return im
