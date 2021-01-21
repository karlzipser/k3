
#,rif.a
"""
python3 k3/scripts/osx/rate_images_in_folder.py\


"""
#,rif.b


from k3.utils import *
key_for = 'key for '
A = get_Arguments(
    {
    	'path':'',
        'links':'',
        'name':'',
        'saved' : False,
        key_for+'quit' : 'q',
        key_for+'Quit no save' : 'Q',
        key_for+'back' : 'j',
        key_for+'forward' : 'k',
        key_for+'save' : 's',
        key_for+'select' : ' ',
        key_for+'un-select' : 'u',
        key_for+'1 step' : '1',
        key_for+'2 step' : '2',
        key_for+'3 step' : '3',
        key_for+'4 step' : '4',
        key_for+'5 step' : '5',
        key_for+'6 step' : '6',
        key_for+'7 step' : '7',
        key_for+'8 step' : '8',
        key_for+'9 step' : '9',
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
    if name_ != '':
        l = '_'+name_ + '.' + l
    else:
        l = '_' + l
    links_ = opjD(l)

imgs = []

fs = sggo(path_,'*')

for f in fs:
    if exname(f).lower() in image_extensions:
        imgs.append(f)

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
        img[:,:10,:] = (255,0,0)
    else:
        img = I[f]
    k = mci(img)
    #k = cv2.waitKey(1)
    return k

def handle_k(k):
    k = k & 0xFF
    for q in A:
        if key_for in q:
            if k == ord(A[q]):
                return q
    return 'key for: unknown'


steps = list(range(1,10))

for i in rlen(steps):
    steps[i] = ord(str(steps[i]))

stp = 1
i = 0

def save():
    if A['name'] == '':
        A['name'] = get_safe_name(input('Enter name => '))
        if A['name'] != '_':
            A['name'] = '_' + A['name']
    os_system('mkdir -p',qtd(d2p(links_,A['name'])),e=1)
    real_paths = []
    for f in selected:
        os_system('ln -s',qtd(opjh(f)),qtd(opjh(d2p(links_,A['name']),fname(f))),e=1,a=1)
        real_paths.append(os.path.realpath(f))
        list_of_strings_to_txt_file(opjD(A['name']),real_paths)
    A['saved'] = True


while True:

    f = imgs[i]

    k = display(f)

    h = handle_k(k)


    if  h == key_for+'quit':
        save()
        break

    if  h == key_for+'Quit no save':
        break

    elif h == key_for+'forward':
        i += stp
        if i >= n:
            i = n-1
        print(i)

    elif h == key_for+'back':
        i -= stp
        if i < 0:
            i = 0
        #print('left arrow',i)
        print(i)

    elif key_for in h and 'step' in h:
        stp = int(A[h])

    elif h == key_for+'select':
        if f not in selected:
            selected.append(f)
            selected = sorted(selected)
            print('+',f)
        else:
            pass
        i += stp
        if i >= n:
            i = n-1
        print(i)

    elif h == key_for+'un-select':
        if f not in selected:
            pass
        else:
            selected.remove(f)
            print('-',f)


    elif h == key_for+'save':
        save()




DONE = True

if False:#not A['saved']:
    s = input('Save? [y]/n ')
    if s == 'n':
        pass
    else:
        save()

#EOF
