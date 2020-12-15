#!/usr/bin/env python3

"""#,show.a

python3 k3/misc/show/show.py \
    --rcratio 1.2 \
    --Bload_Arguements True \

#,show.b"""


from k3 import *
import k3.misc.show.key_counter as key_counter


A = get_Arguments(Defaults={
    'imgs':sggo(opjh('Pictures/*.jpg')),
    'extent' : 256,
    'ignore_underscore':True,
    'padval':0,
    'padsize':5,
    'rcratio':1.1,#1.618,
    'extent2': 350,
    'last_print':'---',
    'last_k':None,
    'Bload_Arguements':True,
    'img_display_list':[],
    'Img_buffer':{},
    'starttime':time.time(),
    'lst':[],
    'Keys':{},
})

D = Bload('show_keys',starttime=0)
if D is None:
    Bsave(A['Keys'],'show_keys')
else:
    A['Keys'] = D

image_info_area_height = 100

def handle_events(event):

    time.sleep(0.01) # needed to allow main tread time to run

    if A['Bload_Arguements']:
        lst_bkp = A['imgs']
        if Bload('reader',Dst=A,starttime=A['starttime']):
            if len(A['imgs']) == 0:
                A['imgs'] = lst_bkp
            A['img_display_list'] = []

    _show()

    x, y, k = event.xdata, event.ydata, event.key

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
                            if A['last_print'] != s or A['last_k'] != k:
                                A['last_print'] = s
                                A['last_k'] = k
                                if True:#k == ' ':
                                    clp('\n'+qtd(s),'`---')
                                    try:
                                        print(key_counter.get_key_str(A['Keys'][I['file']]))
                                    except:
                                        pass
                                img = resize_to_extent(
                                        A['Img_buffer'][I['file']],
                                        A['extent2'],
                                    )
                                q = zeros((image_info_area_height,shape(img)[1],3),np.uint8)
                                imgq = np.concatenate((img,q),axis=0) 
                                fontsize = 0.4
                                cv2.putText(
                                    imgq,
                                    pname(s)+'/',
                                    (10,shape(imgq)[0]-30),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    fontsize,
                                    (150,150,150),
                                    1,
                                    cv2.LINE_AA
                                )
                                cv2.putText(
                                    imgq,
                                    fname(s),
                                    (10,shape(imgq)[0]-10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    fontsize,#.3,
                                    (150,150,150),
                                    1,
                                    cv2.LINE_AA
                                )                                
                                mci(
                                    imgq,
                                    title='mci'
                                )
                                if k is not None and k != ' ':
                                    A['lst'].append({
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
                                        A['lst'],
                                        'show'
                                    )
                                    
                                    if I['file'] not in A['Keys']:
                                        A['Keys'][I['file']] = {}
                                    key_counter.account_for_key(A['Keys'][I['file']],k)
                                    clp('\n'+"'"+k+"'",':',qtd(fname(s)),'`--rb')
                                    print(key_counter.get_key_str(A['Keys'][I['file']]))
                                    Bsave(A['Keys'],'show_keys')
                                return


def _get_image_buffer():

    from pathlib import Path

    change = False

    for f in A['imgs']:

        if f in A['Img_buffer']:
            continue

        if f[0] == '_' and A['ignore_underscore']:
            continue

        sf = Path(f).resolve().as_posix()
        try:
            A['Img_buffer'][f] = zimread(sf)
            cb('loaded',fname(f))
            change = True
        except:
            try:
                del A['Img_buffer'][f]
            except:
                pass
            cE("Couldn't read",sf)

    if change:
        A['img_display_list'] = []


def _make_image_display_list():

    if len(A['img_display_list']) > 0:
        return

    blank = zeros((A['extent'],A['extent'],3),np.uint8)

    ctr = 0
    for f in A['imgs']:
        ctr += 1
        Img_display = {
            'file':f,
            'extent':A['extent'],
            'resized_img':None,
            'square_embeding':None,
            'corner_x':0,
            'corner_y':0,
            }

        Img_display['resized_img'] = resize_to_extent( A['Img_buffer'][f], A['extent'] )

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
    A['cols'] = int(A['rcratio']*sqrt(len(A['img_display_list'])))
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
        A['fig'] = figure('fig',facecolor="0.0")
    mi(A['bkg_image'],'fig')
    A['fig'].tight_layout(pad=0)
    spause()


def _show():
    _get_image_buffer()
    _make_image_display_list()


def main():
    _show()
    cid0 = A['fig'].canvas.mpl_connect('key_press_event', handle_events)
    cid1 = A['fig'].canvas.mpl_connect('button_press_event', handle_events)
    cid2 = A['fig'].canvas.mpl_connect('motion_notify_event', handle_events)
    plt.pause(10**9)


if __name__ == '__main__':
    main()


#EOF
