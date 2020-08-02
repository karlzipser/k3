from k3.vis3 import *

import argparse

try:
    #assert(False)
    os.system('mkdir -p '+opjh('Logs'))
    f = most_recent_file_in_folder(opjh('Logs'),str_elements=[fname(__file__)])
    L = lo(f)
except:
    L = {'full_paths':{},'filenames':{}}




par = argparse.ArgumentParser(
    prog='mi',
    description='use mi from command line',
    fromfile_prefix_chars='@',
    add_help=True,
); aa = par.add_argument

aa(
    '-f',
    nargs="+",
    default=[],
    help='space-separated list of image files to show',
)

aa(
    '-p',
    nargs="+",
    default=[],
    help='space-separated list of paths',
)

aa(
    '-r',
    action='store',
    type=int,
    required=False,
    default=1, 
    help='raw_enter option, 0 or 1',
)

aa(
    '--mwidth',
    action='store',
    type=int,
    required=False,
    default=-1, 
    help='max width',
)

aa(
    '--mheight',
    action='store',
    type=int,
    required=False,
    default=-1, 
    help='max height',
)

aa("-o", nargs='?',
    const=True, default=False,
    help="one image at a time")

aa("-d", nargs='?',
    const=True, default=False,
    help="descend directories collecting images")

aa("--rnd", nargs='?',
    const=True, default=False,
    help="show in random order")



args = par.parse_args()

print(args)

lst = []

lst += args.f


import imghdr
lst0 = []
for p in args.p:
    if args.d:
        lst0 += get_list_of_files_recursively(p,'*',FILES_ONLY=True)
    else:
        lst0 += sggo(p,'*')

#kprint(lst0,t='lst0',r=1)

for l in lst0:
    #print l
    try:
        if imghdr.what(l) is not None:
            lst.append(l)
    except:
        pass
if args.rnd:
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
min_width,min_height = 400,400

g = zeros((intr(max_height*1.),intr(max_width*1.),3),np.uint8)
for p in lst:
    img0 = imread(p)
    img = cv2.cvtColor(img0,cv2.COLOR_BGR2RGB)
    img = get_resized_img(img,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
    f = fname(p)

    part1 = cf(fname(p),'`',pname(p),'`--d')
    if shape(img0) == shape(img):
        part2 = cf(shape(img0)[:2])
    else:
        part2 = cf(shape(img0)[:2],'`','-->',shape(img)[:2],'`r-b')
    clp(part1,part2)

    g *= 0
    img = place_img_f_in_img_g(0,0,img,g,f_center=True,center_in_g=True)
    cv2.namedWindow(f)
    cv2.moveWindow(f,int((screen_sz[0]-max_width)/2),0)

    k = mci(img,title=f)

    if args.o:
        e = getch()
        if p not in L:
            L['full_paths'][p] = []
        L['full_paths'][p].append((e,time.time()))

        CA()
        if e in ['q','Q','quit','exit']:
            sys.exit()

if not args.o and args.r:
    raw_enter()
so(L,opjh('Logs',fname(__file__)+'.'+str(int(time.time()))+'.log'))
