#!/usr/bin/env python3

"""#,s1a

python3 k3/drafts/show1.py \
    --src /Users/karlzipser/iCloud_Links/jpeg/2020 \
    --pattern '*.jpeg' \
    --rcratio 1.2 \
    --Bload_Arguements True \
#,s1b"""


from k3 import *
from pathlib import Path



Defaults={
    'src':opjh('iCloud_Links/jpeg'),
    'pattern': '*.jpeg',
    'extent' : 256,
    'ignore_underscore':True,
    'padval':127,
    'padsize':5,
    'rcratio':1.1,#1.618,
    'extent2': 350,

    'max_num_images': 20,

    'last_print':'---',
    'last_k':None,

    'Bload_Arguements':True,
    'src_pattern':'',
    'img_display_list':[]
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
        return cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)
    else:
        print('no resizing')
        return img



lst = []

timer = Timer(10)

def mouse_move(event):

    time.sleep(0.01) # needed to allow main tread time to run

    if False:#timer.check():
        timer.reset()        
        Bsave(
            {
                'max_num_images':randint(16),
                'img_display_list':[],
                'padsize':randint(50),
                'padval':randint(256),
                'extent2': 100+randint(250),
                'rcratio': 2*rnd(1),
            },
            'show1',
        )

    if A['Bload_Arguements']:
        Bload('show1',Dst=A)

    _show()

    x, y, k = event.xdata, event.ydata, event.key

    if k == ' ':
        plot([0,500],[0,500])

    if k == 'r':
        mi(A['bkg_image']); fig.tight_layout(pad=0); spause()

    if k == 'q':
        cv2.destroyAllWindows()
        CA()
        sys.exit()

    if x is None:
        return

    padsize = A['padsize']

    if 'img_display_list' in A:
        for I in A['img_display_list']:
            if y >= I['corner_y']+padsize:
                if y <= I['corner_y']+padsize+A['extent']:
                    if x >= I['corner_x']+padsize:
                        if x <= I['corner_x']+padsize+A['extent']:
                            s = I['file'].replace(opjh(),'')
                            if A['last_print'] != s or A['last_k'] != k:# or event_button != None or event_dblclick != None:
                                A['last_print'] = s
                                A['last_k'] = k
                                mci(
                                    resize_to_extent(
                                        Img_buffer[I['file']],
                                        A['extent2'],
                                    ),
                                    title='mci'
                                )


                                if True:#try:
                                        if k is not None:
                                            lst.append({
                                                    'writer':__file__,
                                                    'file':I['file'],
                                                    'key':k,
                                                    'time':time.time(),
                                                    'events':{
                                                        'xdata':event.xdata,
                                                        'ydata':event.ydata,
                                                        'x':event.x,
                                                        'y':event.y,
                                                        'key':event.key,

                                                    },
                                            })
                                            Bsave(
                                                lst,
                                                'a'
                                            )

                                """
                                except KeyboardInterrupt:
                                    cE('*** KeyboardInterrupt ***')
                                    text_to_file(A['dst'],"<QUIT>"+'\n',write_mode="a")
                                    sys.exit()
                                except Exception as e:
                                    exc_type, exc_obj, exc_tb = sys.exc_info()
                                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                                    cE('Exception!',exc_type,file_name,exc_tb.tb_lineno)
                                    time.sleep(0.25)
                                """

                                return



def _get_image_buffer():

    if A['src_pattern'] == opj(A['src'],A['pattern']):
        return

    print('Img_buffer loading...')

    fs = sorted(find(A['src'],A['pattern'],e=1))

    for f in fs:

        if len(Img_buffer) > A['max_num_images']:
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
    A['src_pattern'] = opj(A['src'],A['pattern'])
    A['img_display_list'] = []


def _make_image_display_list():

    if len(A['img_display_list']) > 0:
        return

    print('img_display_list being made...')

    blank = zeros((A['extent'],A['extent'],3),np.uint8)
    A['img_display_list'] = []

    ctr = 0
    for f in sorted(kys(Img_buffer)):
        if ctr > A['max_num_images']:
            break
        ctr += 1
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

        A['img_display_list'].append(Img_display)

    _get_list_of_square_embedded_images__and__make_bkg_image()


def _get_list_of_square_embedded_images__and__make_bkg_image():
    A['cols'] = int(A['rcratio']*sqrt(len(kys(Img_buffer))))
    padsize = A['padsize']
    min_x = 10**9
    min_y = 10**9
    max_x = 0
    max_y = 0
    rows,cols = 0,0
    for I in A['img_display_list']:
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

    bkg = zeros((max_y+2*padsize,max_x+2*padsize,3),np.uint8) + A['padval']
    for I in A['img_display_list']:
        bkg[
            I['corner_y']+padsize:I['corner_y']+padsize+A['extent'],
            I['corner_x']+padsize:I['corner_x']+padsize+A['extent'],:] =\
            I['square_embeding']

    A['bkg_image'] = bkg
    _mi()


def _mi():
    if 'fig' not in A:
        A['fig'] = figure('fig',facecolor=".5")
        
    mi(A['bkg_image'],'fig')
    A['fig'].tight_layout(pad=0)
    spause()


def _show():
    _get_image_buffer()
    _make_image_display_list()


def main():
    _show()
    for e in ['motion_notify_event','button_press_event','key_press_event']:
        plt.connect(e, mouse_move)
    input("type 'q' on matrix window to quit")



if __name__ == '__main__':
    main()


#EOF
