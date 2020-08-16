
from k3.vis3 import *

# ffmpeg -i ../fran_at_in_river.MOV -vsync 0 %d.jpeg

ff = sggo(p,'*.jpeg')
p = "/Users/karlzipser/Desktop/temp2/frames"

def show(delay=1,mono=False,crop=None,reverse=False):
	for i in rlen(ff):
		if reverse:
			f = ff[-(i+1)]
		else:
			f = ff[i]
		g = zimread(f)
		if mono:
			g[:,:,0] = g[:,:,1]
			g[:,:,2] = g[:,:,1]
		if crop is not None:
			g = g[crop[0][0]:crop[0][1],crop[1][0]:crop[1][1]]
		mci(g,delay)


if False:
	show()
	show(1,mono=True,crop=((700,1200),(300,800)))
#EOF