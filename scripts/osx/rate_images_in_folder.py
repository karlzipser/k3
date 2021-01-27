
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
        'name':'no_name',
        key_for+'quit' : 'q',
        key_for+'back' : 'j',
        key_for+'forward' : 'k',
        key_for+'act' : 'a',
        key_for+'select' : ' ',
        key_for+'un-select' : 'u',
        key_for+'get name' : 'n',
        key_for+'1 step' : '1',
        key_for+'2 step' : '2',
        key_for+'3 step' : '3',
        key_for+'4 step' : '4',
        key_for+'5 step' : '5',
        key_for+'6 step' : '6',
        key_for+'7 step' : '7',
        key_for+'8 step' : '8',
        key_for+'9 step' : '9',
        'action' : 'ln',
        'r' : False,
        'max' : 100,
        'offset' : 0,
        'ignore' : ['Photos Library'],
        'start' : opjh(),
    },
    file=__file__,
    r=False,
)
if type(A['path']) is list:
    cE("can't handle path with white space now.")
    assert(False)

exec(A_to_vars_exec_str)


if path_ == '':
    path_ = select_folder(start_)[0]

imgs = []

if r_:
    fs = find_files(
        start=path_,
        patterns=['*.jpeg','*.jpg','*.png','*.JPG','*.JPEG','*.JPG','*.PNG'],
        ignore=[],
        recursive=r_
    )   

fs = sorted(fs)
m = min(offset_+max_,len(fs))
fs = fs[offset_:offset_+m]

imgs = fs


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

def _get_name():
    name = get_safe_name(input('Enter name => '))
    if name != '_':
        name = '_' + name
    return name

def act():
    #if A['name'] == '':
    #    A['name'] = get_name()
    l = fname(path_)
    l = re.sub("^.+\.--\.",'',l)
    if action_ == 'links':
        a = 'links.'
    else:
        a = ''
    l = d2n(a,time_str('FileSafe'),'.--.',l )

    if name_ != '':
        l = '_' + name_ + '.' + l
    else:
        l = '_' + l

    links_ = opjD(l)

    os_system('mkdir -p',qtd(d2p(links_,A['name'])),e=1)
    real_paths = []
    for f in selected:
        if action_ == 'ln':
            os_system('ln -s',qtd(opjh(f)),qtd(opjh(d2p(links_,A['name']),fname(f))),e=1,a=1)
        elif action_ == 'cp':
            os_system('cp',qtd(opjh(f)),qtd(opjh(d2p(links_,A['name']))),e=1,a=1)
        elif action_ == 'mv':
            os_system('mv',qtd(opjh(f)),qtd(opjh(d2p(links_,A['name']))),e=1,a=1)

        real_paths.append(os.path.realpath(f))
        list_of_strings_to_txt_file(opjD(d2p('paths',A['name'],'txt')),real_paths)


while True:

    f = imgs[i]

    k = display(f)

    h = handle_k(k)


    if  h == key_for+'quit':
        #act()
        break



    elif h == key_for+'forward':
        i += stp
        if i >= n:
            i = n-1
        cg(d2n(i,') ',f))

    elif h == key_for+'back':
        i -= stp
        if i < 0:
            i = 0
        cb(d2n(i,') ',f))

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
            
    elif h == key_for+'act':
        act()
        break



DONE = True



#EOF
