#!/usr/bin/env python3

"""#,sq0a

python3 k3/drafts/show0.py \
    --src /Users/karlzipser/iCloud_Links/jpg/2020 \
    --pattern '*.jpg' \
    --rcratio 1.2 \
#,sq0b"""


from k3 import *
from pathlib import Path

def find(src,pattern,e=0,r=0,a=1):
    tempfile = opjD(d2p('find','temp',random_with_N_digits(9),'txt'))
    os_system('find',src,'-name',qtd(pattern),">",tempfile,e=e,r=r,a=a)
    find_list = txt_file_to_list_of_strings(tempfile)
    os_system("rm",tempfile)
    return find_list

Defaults={
    'src':opjh('iCloud_Links/jpg'),
    'pattern': '*.jpg',
    'extent' : 256,
    'ignore_underscore':True,
    'padval':127,
    'padsize':32,
    'rcratio':1.1,#1.618,
    'extent2': 700,
}
A = get_Arguments(Defaults)

Img_buffer = {}

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



# Write some Text

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,500)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2




MOUSE_ = {'xy':(-1,-1),'last_print':'---','quit':False}
MOUSE_['text_img'] = np.zeros((128,1024,3), np.uint8)

def mouse_move(event):
    time.sleep(0.001) # needed to allow main tread time to run
    if MOUSE_['quit']:
        sys.exit()
    x, y = event.xdata, event.ydata
    if x is None:
        return

    MOUSE_['xy'] = (x,y)
    if x<10 and y<10:
        print("x<10 and y<10")
        sys.exit()
    if 'img_display_list' in MOUSE_:
        for I in MOUSE_['img_display_list']:
            if y >= I['corner_y']+padsize:
                if y <= I['corner_y']+padsize+A['extent']:
                    if x >= I['corner_x']+padsize:
                        if x <= I['corner_x']+padsize+A['extent']:
                            s = I['file'].replace(opjh(),'')
                            if MOUSE_['last_print'] != s:
                                MOUSE_['last_print'] = s
                                mci(
                                    resize_to_extent(
                                        Img_buffer[I['file']],
                                        A['extent2'],
                                    ),
                                    title='mci'
                                )
                                MOUSE_['text_img'] *= 0
                                cv2.putText(MOUSE_['text_img'],s, 
                                    bottomLeftCornerOfText, 
                                    font, 
                                    fontScale,
                                    fontColor,
                                    lineType)

                                #cv2.putText(MOUSE_['text_img'],d2n(s,' ',MOUSE_['quit']),(10,y), font, 0.5,(255,255,0),1, cv2.LINE_AA)
                                
                                txt = d2n(s,'\n',MOUSE_['quit'])
                                if 'Knot' in txt:
                                    print("if 'Knot' in txt:")
                                    sys.exit()
                                y0, dy = 50, 20
                                for i, line in enumerate(txt.split('\n')):
                                    y = y0 + i*dy
                                    cv2.putText(MOUSE_['text_img'],line,(10,y), font, 0.5,(255,255,0),1, cv2.LINE_AA)
                                    #cv2.putText(img, line, (50, y ), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)

                                mci(MOUSE_['text_img'],title='text_img')
                                return


if 'get image buffer':

    

    fs = find(A['src'],A['pattern'],e=1)


    for f in fs:

        if len(Img_buffer) > 10*10:
            continue

        if f[0] == '_' and A['ignore_underscore']:
            continue

        if f in Img_buffer:
            continue

        sf = Path(f).resolve().as_posix()
        try:
            Img_buffer[f] = zimread(sf)
            cb('loaded',f)
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
    A['cols'] = int(A['rcratio']*sqrt(len(kys(Img_buffer))))
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

mini_menu(A,menu_keys=['extent2'])
MOUSE_['quit'] = True
time.sleep(1)

#EOF
