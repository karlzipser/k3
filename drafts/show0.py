#!/usr/bin/env python3

"""#,sq1a

python3 k3/drafts/show0.py \
    --src /Users/karlzipser/iCloud_Links/jpeg \
    --pattern *.jpeg \
#,sq1b"""
#,a

from k3 import *
from pathlib import Path

def find(src,pattern,e=0,r=0,a=1):
    tempfile = opjD(d2p('find','temp',random_with_N_digits(9),'txt'))
    os_system('find',src,'-name',qtd(pattern),">",tempfile,e=e,r=r,a=a)
    find_list = txt_file_to_list_of_strings(tempfile)
    os_system("rm",tempfile)
    return find_list


A = get_Arguments(
    Defaults={
    'src':opjh('Archived'),
    'pattern': '_preview.jpg',
    'extent' : 256,
    'ignore_underscore':True,
    'padval':127,
    'padsize':32,
    'cols':40,
    }
)

def resize_to_extent(img,extent):
    if extent != max(shape(img)):
        q = extent / max(shape(img))
        scale_percent = 60 # percent of original size
        width = int(img.shape[1] * q)
        height = int(img.shape[0] * q)
        dim = (width, height)
        #print(shape(img),dim)
        return cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)
    else:
        print('no resizing')
        return img


MOUSE_ = {'xy':(-1,-1),'last_print':'---'}
def mouse_move(event):
    x, y = event.xdata, event.ydata
    if x is None:
        return
    #print(int(x),int(y))
    MOUSE_['xy'] = (x,y)
    if 'img_display_list' in MOUSE_:
        for I in MOUSE_['img_display_list']:
            if y >= I['corner_y']+padsize:
                if y <= I['corner_y']+padsize+A['extent']:
                    if x >= I['corner_x']+padsize:
                        if x <= I['corner_x']+padsize+A['extent']:
                            s = I['file'].replace(opjh(),'')
                            if MOUSE_['last_print'] != s:
                                print(s)
                                MOUSE_['last_print'] = s
                                return


if 'get image buffer':

    Img_buffer = {}

    fs = find(A['src'],A['pattern'],e=1)

    for f in fs:

        if f[0] == '_' and A['ignore_underscore']:
            continue

        if f in Img_buffer:
            continue

        sf = Path(f).resolve().as_posix()
        try:
            Img_buffer[f] = zimread(sf)
        except:
            try:
                del Img_buffer[f]
            except:
                pass
            cE("Couldn't read",sf)

if 'make image display list':

    blank = zeros((A['extent'],A['extent'],3),np.uint8)
    img_display_list = []

    for f in kys(Img_buffer):

        Img_display = {
            'file':f,
            'extent':A['extent'],
            'resized_img':None,
            'square_embeding':None,
            'corner_x':0,
            'corner_y':0,
            }

        Img_display['resized_img'] = resize_to_extent( Img_buffer[f], A['extent'] )

        h,w,d = shape(Img_display['resized_img'])
        blank = 0 * blank + A['padval']
        e2 = A['extent']//2
        blank[
            e2-h//2 : e2-h//2+h,
            e2-w//2 : e2-w//2+w,
            :d,
        ] = Img_display['resized_img']
        Img_display['square_embeding'] = blank

        img_display_list.append(Img_display)

if 'get list of square-embedded images':
    A['cols'] = int(1.6*sqrt(len(kys(Img_buffer))))
    padsize = A['padsize']
    l = []
    min_x = 10*9
    min_y = 10^9
    max_x = 0
    max_y = 0
    rows,cols = 0,0
    for I in img_display_list:
        I['corner_x'] = cols * (A['extent'] + padsize)
        I['corner_y'] = rows * (A['extent'] + padsize)
        min_x = min(I['corner_x'],min_x)
        min_y = min(I['corner_y'],min_y)
        max_x = max(I['corner_x']+A['extent'],max_x)
        max_y = max(I['corner_y']+A['extent'],max_y)
        if cols < A['cols']-1:
            cols += 1
        else:
            rows += 1
            cols = 0

    MOUSE_['img_display_list'] = img_display_list

    bkg = zeros((max_y+2*padsize,max_x+2*padsize,3),np.uint8) + A['padval']
    for I in img_display_list:
        bkg[
            I['corner_y']+padsize:I['corner_y']+padsize+A['extent'],
            I['corner_x']+padsize:I['corner_x']+padsize+A['extent'],:] =\
            I['square_embeding']
    #l.append(I['square_embeding'])


fig = figure('fig',facecolor=".5")
#mi(vis_square2(l,padsize=8,padval=padval),'fig')
mi(bkg)
fig.tight_layout(pad=0)
plt.connect('motion_notify_event', mouse_move)
#plt.show()
spause()
raw_enter()





#,b


#EOF
