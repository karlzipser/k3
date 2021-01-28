
#,rif.a
"""
python3 k3/scripts/osx/rate_images_in_folder.py\


"""
#,rif.b


from k3.utils import *
from k3.utils.vis import *
import threading

key_for = 'key for '
A = get_Arguments(
    {
    	('paths',"image search paths. if [], then select interactively"):[],
        ('path','single path instead of paths') : '',
        ('name','name for new folder'):'no_name',
        ('action','action to take on selected images') : 'ln',
        ('r','recursive image file search') : False,
        ('max','max number of images to permit') : 100,
        ('offset','offset within image list') : 0,
        ('ignore','folders to ignore') : ['Photos Library','Photo Booth'],
        ('start','start location for selecting') : opjh(),
        ('extent','image extent, less than zero indicates no change') : -1,
        key_for+'quit' : 'q',
        key_for+'back' : 'j',
        key_for+'forward' : 'k',
        key_for+'act' : 'a',
        key_for+'select' : ' ',
        key_for+'un-select' : 'u',
        key_for+'get action' : 'A',
        key_for+'get name' : 'N',
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

exec(A_to_vars_exec_str)




if path_ != '':
    assert paths_ == []
    paths_ = [path_]
    path_ = ''


if paths_ == []:
    paths_ = select_folders(start_)

#imgs = []

fs = []
for p in paths_:
    fs += find_files(
        start=p,
        patterns=['*.jpeg','*.jpg','*.png','*.JPG','*.JPEG','*.JPG','*.PNG'],
        ignore=[],
        recursive=r_
    )

fs = sorted(fs)
m = min(offset_+max_,len(fs))
fs = fs[offset_:offset_+m]

#imgs = fs

I = {}

n = len(fs)#imgs)
DONE = False

def loader_thread():
    for f in fs:#imgs:
        #kprint(I.keys())
        if DONE:
            #print("returning from loader_thread()")
            return
        if f not in I:
            #print('thread loading',f)
            tmp = zimread(f)

            if extent_ > 0:
                #cE('*** resizeing')
                tmp = resize_to_extent(tmp,extent_)

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

        if extent_ > 0:
            #cE('resizeing')
            tmp = resize_to_extent(tmp,extent_)

        I[f] = tmp
        print('read',f)
    
    if f in selected:
        img = I[f].copy()
        img[:,:10,:] = (255,0,0)
    else:
        img = I[f]
    k = mci(img)
    cv2.moveWindow('mci', 20, 20)
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

def _get_action():
    a = get_safe_name(input('Enter action => '))
    if a not in ['cp','ln','mv']:
        cE(qtd(a),"is not in ['cp','ln','mv'[")
        return ''
    else:
        return a

def act():
    #if A['name'] == '':
    #    A['name'] = get_name()
    l = fname(paths_)
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

def blank_out_path(a0,b0):
    a = a0.split('/')
    b = b0.split('/')
    c = []
    for i in range(min(len(a),len(b))):
        if a[i] == b[i]:
            c.append('.'*len(a[i]))
        else:
            break
    #d = '.'.join(c)
    e = []
    for i in range(i,len(b)):
        e.append(b[i])
    return c+e
    #return '/'.join([d]+e) 



def _blank_out_string(a,b):
    c = []
    i = 0
    for i in range(min(len(a),len(b))):
        if a[i] == b[i]:
            c.append('.')
        else:
            break
    for i in range(i+1,len(b)):
        c.append(b[i])
    return ''.join(c) 

def print_list_segment(lst,i,a=0,b=1,f0=cg,f1=cb):
    if i-a < 0:
        c = 0
    else:
        c = i-a
    if i + b > len(lst):
        d = len(lst)
    else:
        d = i + b
    for j in range(c,d):
        if j == i:
            f = f0
            clr = '`--rb'
        else:
            f = f1
            clr = '`--d'

        s = pname(lst[j])
        if s[0] == '/':
            s = s[1:]
        s = s.split('/')#.remove('')
        #cy(s)
        #s = re.sub('^.*Users\/'+username+'\/','*~/',s)
        v = fname(lst[j])
        #print(s)
        #while username in s:
        #    s.pop(0)
        s = '/'.join(s)
        #print(s,v)
        if j > c:
            q = pname(lst[j-1])
            if q[0] == '/':
                q = q[1:]
            q = q.split('/')#.remove('')
            #cg(q)
            #while username in q:
            #    q.pop(0)
            q = '/'.join(q)
            #q = re.sub('^.*Users\/'+username+'\/','*~/',q)
        else:
            q = ''
        s = blank_out_path(q,s)


            #if v == username:
            #    s = ['~'] + s
        #cm(s)
        clp(d2n(j,') ',s,v),clr)
        #f(d2n(j,') ',opj(s,v)))

print_list_segment(fs,i,a=3,b=3)



while True:

    f = fs[i]#imgs[i]

    k = display(f)

    h = handle_k(k)


    if  h == key_for+'quit':
        #act()
        break



    elif h == key_for+'forward':
        i += stp
        if i >= n:
            i = n-1
        clear_screen()
        print_list_segment(fs,i,a=3,b=3)
        #cg(d2n(i,') ',f))

    elif h == key_for+'back':
        i -= stp
        if i < 0:
            i = 0
        clear_screen()
        print_list_segment(fs,i,a=3,b=3)
        #cb(d2n(i,') ',f))

    elif key_for in h and 'step' in h:
        stp = int(A[h])

    elif h == key_for+'select':
        if f not in selected:
            selected.append(f)
            selected = sorted(selected)
            #print('+',f)
        else:
            pass
        i += stp
        if i >= n:
            i = n-1
        #print(i)

    elif h == key_for+'un-select':
        if f not in selected:
            pass
        else:
            selected.remove(f)
            #print('-',f)

    elif h == key_for+'get name':
        A['name'] = _get_name()
        name_ = A['name']

    elif h == key_for+'get action':
        a = _get_action()
        if len(a) > 0:
            A['action'] = a
            action_ = A['action']
            
    elif h == key_for+'act':
        act()
        break



DONE = True



#EOF
