from k3.utils.misc.printing import *
from k3.utils.misc.sys import *


def load_text_list(path,unique=False):
    try:
        lst = txt_file_to_list_of_strings(path)
        print('loaded',path)
    except:
        cE(path,'not loaded')
        lst = []
    if unique:
        lst = sorted(list(set(lst)),key=natural_keys)
    return lst


def find_images_from_paths(paths,start=opjh(),recursive=True):
    if paths == []:
        paths = select_folders(start)
    fs = []
    for p in paths:
        fs += find_files(
            start=p,
            patterns=['*.jpeg','*.jpg','*.png','*.JPG','*.JPEG','*.JPG','*.PNG'],
            ignore=[],
            recursive=recursive
        )
    return fs





def display(f,Images={},extent=-1,selected=[],notable=[]):
    from k3.utils.vis import zimread,mci,cv2,resize_to_extent
    if f not in Images:
        Images[f] = 'temp'
        tmp = zimread(f)

        if extent > 0:
            #cE('resizeing')
            tmp = resize_to_extent(tmp,extent)

        Images[f] = tmp
        print('read',f)
    
    if f in selected or f in notable:
        img = Images[f].copy()
    else:
        img = Images[f]

    if f in notable:
        img[-5:,:,:] = (100,200,100)

    if f in selected:
        img[:,:10,:] = (255,0,0)

    k = mci(img)
    cv2.moveWindow('rif', 20, 20)
    #k = cv2.waitKey(1)
    return k

key_for = 'key for '
def handle_k(k,A):
    k = k & 0xFF
    for q in A:
        if key_for in q:
            if k == ord(A[q]):
                return q
    return 'key for: unknown'



def image_loader_thread(D={'Images':{},'done':False,'fs':{},'extent':400}):
    from k3.utils.vis import zimread,resize_to_extent
    Images = D['Images']
    for f in D['fs']:
        if D['done']:
            return
        if f not in Images:
            tmp = zimread(f)
            if D['extent'] > 0:
                tmp = resize_to_extent(tmp,D['extent'])
            if f not in Images:
                Images[f] = tmp
        time.sleep(0.1)
    cg('loader_thread() finished')


#EOF
