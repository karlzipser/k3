
#,rif.a
"""
python3 k3/scripts/osx/rate_images_in_folder.py\


"""
#,rif.b
"""
    --path scratch/2021/1/10/timelapse.10Jan21_14h52m26s\

1625+52 - 550
"""



from k3.utils import *

A = get_Arguments(
    {
    	'path':'',
        'links':'',
    },
    file=__file__,
    r=False,
)
if type(A['path']) is list:
    A['path'] = ' '.join(A['in'])

exec(A_to_vars_exec_str)

image_extensions = ['jpg','jpeg','png']


if path_ == '':
    path_ = select_folder(opjh())[0]

if links_ == '':
    #l = fname(path_).split('.--.')[1]
    l = fname(path_)
    l = re.sub("^.+\.--\.",'',l)
    l = d2n('links.',time_str('FileSafe'),'.--.',l )
    links_ = opjD(l)

imgs = []
fs = sggo(path_,'*')
#print('fs',fs)
for f in fs:
    if exname(f).lower() in image_extensions:
        imgs.append(f)

#kprint(imgs)
I = {}


n = len(imgs)
DONE = False

def loader_thread():
    for f in imgs:
        #kprint(I.keys())
        if DONE:
            #print("returning from loader_thread()")
            return
        if f not in I:
            #print('thread loading',f)
            tmp = zimread(f)
            if f not in I:
                I[f] = tmp
        time.sleep(0.1)
    cg('loader_thread() finished')

threading.Thread(target=loader_thread).start()

selected = []
fontsize = 6

def display(f):
    if f not in I:
        I[f] = 'temp'
        tmp = zimread(f)
        I[f] = tmp
        print('read',f)
    
    if f in selected:
        img = I[f].copy()
        """
        cv2.putText(
            img,
            '*',
            (10,30),#shape(img)[0]-30),
            cv2.FONT_HERSHEY_SIMPLEX,
            fontsize,
            (255,0,0),
            2,
            cv2.LINE_AA
        )
        """
        img[:,:10,:] = (255,0,0)
    else:
        img = I[f]
    k = mci(img)
    #k = cv2.waitKey(1)
    return k

steps = list(range(1,10))
for i in rlen(steps):
    steps[i] = ord(str(steps[i]))

stp = 1
print(stp)
i = 0


def save(name=''):
    if name=='':
        name = get_safe_name(input('Enter name => '))
    os_system('mkdir -p',qtd(d2p(links_,name)),e=1)
    for f in selected:
        os_system('ln -s',qtd(opjh(f)),qtd(opjh(d2p(links_,name),fname(f))),e=1,a=1)


while True:

    f = imgs[i]

    k = display(f)


    #if k != -1:
    #    print('k =',k)

    if  k & 0xFF == ord('q'):
        break

    elif k == 3: # right arrow
        i += stp
        if i >= n:
            i = n-1
        print(i)


    elif k == 2: # left arrow
        i -= stp
        if i < 0:
            i = 0
        #print('left arrow',i)
        print(i)

    elif k & 0xFF in steps:
        stp = k-48
        if stp < 1:
            stp = 1
        if stp > 9:
            stp = 9

    elif  k & 0xFF == ord(' '):
        print('space',i,f)
        if f not in selected:
            selected.append(f)
            selected = sorted(selected)
            print('+',f)
        else:
            pass
            #selected.remove(f)
            #print('-',f)
        #os_system('rm',opjh(links_,'*.*'),a=1,e=1)
        i += stp
        if i >= n:
            i = n-1
        print(i)

    elif  k & 0xFF == ord('u'):
        #print('u',i,f)
        if f not in selected:
            pass
        else:
            selected.remove(f)
            print('-',f)
        #os_system('rm',opjh(links_,'*.*'),a=1,e=1)


    elif  k & 0xFF == ord('s'):
        save()


DONE = True

#EOF
