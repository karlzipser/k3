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


    'dst':opjD('w1234.txt'),
    'write_mode':'a',
    'start_empty':True,

}
A = get_Arguments(Defaults)

if A['start_empty']:
    os_system('rm',A['dst'])


Img_buffer = {}

def resize_to_extent(img,extent):
    if extent != max(shape(img)):
        q = extent / max(shape(img))
        scale_percent = 60 # percent of original size
        width = int(img.shape[1] * q)
        height = int(img.shape[0] * q)
        dim = (width, height)
        return cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)
    else:
        print('no resizing')
        return img


MOUSE_ = {'xy':(-1,-1),'last_print':'---','quit':False,'last_k':None}

def mouse_move(event):

    time.sleep(0.001) # needed to allow main tread time to run

    x, y, k = event.xdata, event.ydata, event.key
    if k == 'q':
        cv2.destroyAllWindows()
        CA()
        #sys.exit()

    if x is None:
        return


    if 'img_display_list' in MOUSE_:
        for I in MOUSE_['img_display_list']:
            if y >= I['corner_y']+padsize:
                if y <= I['corner_y']+padsize+A['extent']:
                    if x >= I['corner_x']+padsize:
                        if x <= I['corner_x']+padsize+A['extent']:
                            s = I['file'].replace(opjh(),'')
                            if MOUSE_['last_print'] != s or MOUSE_['last_k'] != k:
                                MOUSE_['last_print'] = s
                                MOUSE_['last_k'] = k
                                mci(
                                    resize_to_extent(
                                        Img_buffer[I['file']],
                                        A['extent2'],
                                    ),
                                    title='mci'
                                )

                                if False:
                                    MOUSE_['text_img'] *= 0
                                    cv2.putText(MOUSE_['text_img'],s, 
                                        bottomLeftCornerOfText, 
                                        font, 
                                        fontScale,
                                        fontColor,
                                        lineType)

                                try:
                                        if k is not None:
                                            text_to_file(
                                                A['dst'],
                                                d2s(
                                                    '(',
                                                    qtd(I['file']),
                                                    ',',
                                                    qtd(k),
                                                    ',',
                                                    qtd(d2c(time.time(),random_with_N_digits(3))),
                                                    ')',
                                                ),
                                                write_mode=A['write_mode'],
                                            )

                                except KeyboardInterrupt:
                                    cE('*** KeyboardInterrupt ***')
                                    text_to_file(A['dst'],"<QUIT>"+'\n',write_mode="a")
                                    sys.exit()
                                except Exception as e:
                                    exc_type, exc_obj, exc_tb = sys.exc_info()
                                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                                    cE('Exception!',exc_type,file_name,exc_tb.tb_lineno)
                                    time.sleep(0.25)

                                return


if 'get image buffer':

    
    fs = find(A['src'],A['pattern'],e=1)


    for f in fs:

        if len(Img_buffer) > 6*6:
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

while True:
    fig = figure('fig',facecolor=".5")
    mi(bkg)
    fig.tight_layout(pad=0)
    plt.connect('motion_notify_event', mouse_move)
    plt.connect('key_press_event', mouse_move)
    spause()
    input("type 'q' on matrix window to quit")
    mini_menu(A)
#EOF
