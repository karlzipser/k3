from k3.vis3 import *

import argparse

par = argparse.ArgumentParser(
	prog='mi',
    description='use mi from command line',
    fromfile_prefix_chars='@',
    add_help=True,
); aa = par.add_argument

aa(
	'-l',
	nargs="+",
	default=[],
    help='space-separated list of images to show',
)

aa(
	'-r',
	action='store',
	type=int,
	required=False,
	default=1, 
	help='raw_enter option, 0 or 1',
)
"""
aa(
	'--rnd',
	action='store',
	type=int,
	required=False,
	default=1, 
	help='randomize display order, 0 or 1',
)
"""
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
                        help="Activate nice mode.")

aa("--rnd", nargs='?',
                        const=True, default=False,
                        help="Activate nice mode.")

aa(
	'-p',
	action='store',
	type=str,
	required=False,
	default='', 
	help='path to images',
)

args = par.parse_args()

print(args)

lst = args.l

if args.p != '':
	import imghdr
	lst0 = sggo(args.p,'*')
	lst = []
	for l in lst0:
		if imghdr.what(l) is not None:
			lst.append(l)

if args.rnd:
	random.shuffle(lst)


from Quartz import CGDisplayBounds
from Quartz import CGMainDisplayID

def screen_size():
    mainMonitor = CGDisplayBounds(CGMainDisplayID())
    return (mainMonitor.size.width, mainMonitor.size.height) 

screen_sz = screen_size()

max_width,max_height = screen_sz[0]*0.9,screen_sz[1]*0.9
min_width,min_height = 400,400

g = zeros((intr(max_height*1.),intr(max_width*1.),3),np.uint8)
for p in lst:
	img0 = imread(p)
	img = cv2.cvtColor(img0,cv2.COLOR_BGR2RGB)
	img = get_resized_img(img,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
	f = fname(p)
	clp(f,shape(img0),shape(img))
	g *= 0
	img = place_img_f_in_img_g(0,0,img,g,f_center=True,center_in_g=True)
	cv2.namedWindow(f)
	cv2.moveWindow(f,int((screen_sz[0]-max_width)/2),0)
	#cv2.namedWindow(f,flags=cv2.WINDOW_GUI_NORMAL)
	#cv2.setWindowProperty(f, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
	mci(img,title=f)
	if args.o:
		e = getch()
		CA()
		if e in ['q','Q','quit','exit']:
			sys.exit()

if not args.o and args.r:
	raw_enter()
