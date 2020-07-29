#,a
from k3.vis3 import *

cr('r')
cg('g')
cb('b')
clp('testing','`rgb','various','`ybu','colors','`m')

raw_enter()

a = z55(rndn(64,64,3))
img_path = opjD('temp.jpg')
imsave(img_path,a)
b = imread(img_path)

mi(b)
mci(b,scale=4)

raw_enter();CA()

os.system('rm '+img_path)

hist(rndn(10000))
spause()
raw_enter();CA()

xy = rndn(1000,2)
pts_plot(xy)
plt_square()
spause()
raw_enter();CA()


#,b

#EOF

