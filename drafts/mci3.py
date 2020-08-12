from k3.vis3 import *


def read_image_to_IMAGE_DIC(IMAGE_DIC):

    while True:
        #print(time.time())
        if IMAGE_DIC['del_lst'] is None:
            break

        if len(IMAGE_DIC['images']) <= 100 - len(IMAGE_DIC['del_lst']):

            p = IMAGE_DIC['lst'][ IMAGE_DIC['ctr'] ]
            IMAGE_DIC['ctr'] += 1
            img0, theta = load_image_with_orientation(p)
            img = get_resized_img(img0,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
            IMAGE_DIC['images'][p] = img,shape(img0),theta

        else:
            time.sleep(0.1)
                        
    print("exiting read_image_to_IMAGE_DIC")

    





def get_args():
    
    import argparse

    par = argparse.ArgumentParser(
        prog='mci3.py',
        description='display and rate from command line',
        fromfile_prefix_chars='@',
        add_help=True,
    ); aa = par.add_argument


    aa(
        '--files',
        '-f',
        nargs="+",
        default=[],
        help='space-separated list of image files to show',
    )
    aa(
        '--paths',
        '-p',
        nargs="+",
        default=[],
        help='space-separated list of paths',
    )
    aa(
        '--ignore_paths',
        '-ip',
        nargs="+",
        default=[],
        help='space-separated list of paths to ignore',
    )


    aa(
        '--change',
        '-c',
        nargs='?',
        const=True,
        default=False,
        help="allow change",
    )    
    aa(
        '--random',
        '-r',
        nargs='?',
        const=True,
        default=False,
        help="randomize display order",
    )
    aa(
        '--progressive_range',
        '-pr',
        nargs='?',
        const=True,
        default=False,
        help='view with progressive rating range',
    )
    aa(
        "--hist",
        nargs='?',
        const=True, default=False,
        help="make histogram of ratings"
    )
    aa(
        "--cmd_lines",
        nargs='?',
        const=True,
        default=False,
        help="print command lines used so far"
    )
    aa(
        "--view_once",
        "-vo",
        nargs='?',
        const=True,
        default=False,
        help="don't view image if already rated",
    )
    aa(
        "--slideshow",
        "-s",
        nargs='?',
        const=True,
        default=False,
        help="slideshow mode",
    )
    aa(
        "--descend",
        "-d",
        nargs='?',
        const=True,
        default=False,
        help="descend directories collecting images"
    )

    aa(
        '--screen_pro',
        '-sp',
        action='store',
        type=float,
        required=False,
        default=0.9, 
        help='proportion of screen to use',
    )
    aa(
        '--topic',
        '-tp',
        action='store',
        type=str,
        required=True,
        default='no_name', 
        help='name of topic of images',
    )
    aa(
        '--add_as',
        action='store',
        type=float,
        required=False,
        default=0, 
        help='add images as rating given ',
    )
    aa(
        '--min_rating',
        '-mn',
        action='store',
        type=float,
        required=False,
        default=0, 
        help='minmum rating (1-9) to display',
    )
    aa(
        '--max_rating',
        '-mx',
        action='store',
        type=float,
        required=False,
        default=10, 
        help='maximum rating (1-9) to display',
    )
    aa(
        '--mwidth',
        action='store',
        type=int,
        required=False,
        default=400, 
        help='min width',
    )
    aa(
        '--window_x',
        action='store',
        type=int,
        required=False,
        default=-1, 
        help='window x upper left corner',
    )
    aa(
        '--window_y',
        action='store',
        type=int,
        required=False,
        default=-1, 
        help='window y upper left corner',
    )
    aa(
        '--view_n',
        action='store',
        type=int,
        required=False,
        default=0, 
        help='rate up to n views',
    )
    aa(
        '--mheight',
        action='store',
        type=int,
        required=False,
        default=400, 
        help='min height',
    )
    aa(
        '--seconds',
        '-sc',
        action='store',
        type=float,
        required=False,
        default=1.0, 
        help='slideshow display seconds',
    )

    args = par.parse_args()

    return args




def load_and_display_img(p,g,IMAGE_DIC,delay):

    if p not in IMAGE_DIC['images']:
        cb(fname(p),"not in IMAGE_DIC, loadiing.")
        img0, theta = load_image_with_orientation(p)
        img = get_resized_img(img0,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
        IMAGE_DIC['images'][p] = img,shape(img0),theta
        img0_shape = shape(img0)
    else:
        img,img0_shape,theta = IMAGE_DIC['images'][p]

    IMAGE_DIC['viewed_in_this_session'].append(p)

    if p not in IMAGE_DIC['del_lst']:
        IMAGE_DIC['del_lst'].append(p)

    #f = fname(p)
    if False:
        if theta:
            c = '`y'
        else:
            c = '`'

    

    if False:
        if img0_shape == shape(img):
            part2 = cf(img0_shape[:2],c)
        else:
            part2 = cf(img0_shape[:2],c,'-->',shape(img)[:2],'`m',s0='')
    
    #h = cf(part1,part2)

    img = place_img_f_in_img_g(0,0,img,0*g,f_center=True,center_in_g=True)

    w = 'images'
    cv2.namedWindow(w)
    if args.window_x < 0:
        wx = int((SCREEN_RESOLUTION[0]-max_width)/2)
    else:
        wx = args.window_x
    if args.window_y < 0:
        wy = 0
    else:
        wy = args.window_y
    cv2.moveWindow(w,wx,wy)

    k = mci(img,title=w,delay=delay)
    if k >= 0:
        e = chr(k)
        print(e)
    else:
        e = ''

    return e


def rndrect(x=200,y=100):
    return z55(rndn(y,x,3))



def process_getch(p,i,change,e):

    if e in ['s']:
        p_safe = get_safe_name(p.replace('/','__'),safe_chars=['.','-'])
        s = d2s("cp",'\"'+p+'\"',opjD(p_safe))
        os_system(s,e=1)

    elif str_is_int(e):
        if args.change:
            L['full_paths'][p].append((e,int(time.time())))
            #kprint(L['full_paths'][p])
            #cg(p,L['full_paths'][p],"len(L['full_paths']) =",len(L['full_paths']))
            i += 1
            change = True
        else:
            raw_enter('change not allowed')

    elif e == 'c':
        if args.change:
            L['full_paths'][p] = []
            clp('Cleared',fname(p),'`ybb')
        #i += 1

    elif e == 'p':
        print('back',i)
        i -= 1

    elif e == ' ':
        i += 1

    elif e in ['q']:
        return 'quit',change



    else:
        clp("unused key",'`rwb')

    return i,change







def __save_L(L):
    so(L,opjh('Logs',fnamene(__file__),args.topic,d2p(fnamene(__file__),args.topic,str(int(time.time())),'log')))

def save_L(L):
    file_path = opjh('Logs',fnamene(__file__),args.topic,d2p(fnamene(__file__),args.topic,str(int(time.time())),'log'))
    latest_path = opj(pname(file_path),'latest.pkl')
    so(L,file_path)
    os.system(d2s('rm',latest_path))
    os.system(d2s('ln -s',file_path,latest_path))


def setup_L():
    try:
        os.system('mkdir -p '+opjh('Logs',fnamene(__file__),args.topic))
        f = most_recent_file_in_folder(opjh('Logs',fnamene(__file__),args.topic),str_elements=[fnamene(__file__)])
        L = lo(f)
        del_lst = []
        for p in L['full_paths']:
            if len(L['full_paths'][p]) == 0:
                del_lst.append(p)
        for p in del_lst:
            del L['full_paths'][p]
    except:
        L = {}
        clp("L = {}",r=1)

    for q in ['sys.argv','Args']:
        if q not in L:
            L[q] = []
    for q in ['full_paths']:
        if q not in L:
            L[q] = {}
    L['sys.argv'].append( (sys.argv,int(time.time()) ))
    L['Args'].append( (vars(args),int(time.time()) ))
    return L



def print_command_lines(L):
    ctr = 0
    for l in L['sys.argv']:
        if is_even(ctr):
            c = '`---'
        else:
            c = '`---'
        for i in range(1,len(l[0])):
            if "/" in l[0][i]:
                l[0][i] = '\"' + l[0][i] + '\"'
        clp(' '.join(l[0]),c,time_str(t=l[1],mode='Pretty2'),'`--d')
        ctr += 1



def skip_f(f,verbose=True):
    skip = False
    try:
        for a in args.ignore_paths:
            if a in f:
                if verbose: clp('ignore_paths: skip',a,f)
                skip = True
                break
        if skip:
            return True

        for a in args.paths:
            if a not in f:
                if verbose: clp('skip',a,f)
                skip = True
                break
        if skip:
            return True
    except:
        pass
    return skip



def get_list_of_files(L):

    lst = []

    if args.slideshow or args.min_rating > 0 or args.max_rating < 10 or args.progressive_range:

        if len(L['full_paths']) == 0:
            clp("warning, len(L['full_paths']) == 0",
                "with args.slideshow or args.min_rating > 0 or args.max_rating < 10",
                "or args.progressive_range True",'`wrb')

        for f in L['full_paths']:

            if skip_f(f):
                continue

            if len(L['full_paths'][f]) > 0:
                try:
                    a = 0
                    for b in L['full_paths'][f]:
                        a += int(b[0])
                    r = a / (1.0*len(L['full_paths'][f]))

                    if args.progressive_range:
                        if start_timer.time() < 30:
                            if r >= 4 and r <= 5:
                                lst.append(f)
                        elif start_timer.time() < 60:
                            if r >= 4 and r <= 6:
                                lst.append(f)
                        elif start_timer.time() < 90:
                            if r >= 5 and r <= 7:
                                lst.append(f)
                        elif start_timer.time() < 120:
                            if r >= 6 and r <= 8:
                                lst.append(f)
                        else:
                            if r >=7 and r < 10:
                                lst.append(f)
                    else:                
                        if r >= args.min_rating and r <= args.max_rating:
                            lst.append(f)
                        else:
                            pass
                except KeyboardInterrupt:
                    cr('*** KeyboardInterrupt ***')
                    IMAGE_DIC['del_lst'] = None
                    if change:
                        save_L(L)
                    sys.exit()
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print('Exception!')
                    print(d2s(exc_type,file_name,exc_tb.tb_lineno))
    else:
        #c
        import imghdr
        lst += args.files
        lst0 = []
        for p in args.paths:
            #cy(p,r=1)
            if args.descend:
                #cg('here!',r=1)
                q = get_list_of_files_recursively(p,'*',FILES_ONLY=True,ignore_underscore=False)
                u = []
                for v in q:
                    #cm(v)
                    if p not in v:
                        if v[0] == '/':
                            v = v[1:]
                        u.append(opj(p,v))
                        #cy(p,v,opj(p,v))
                        #cm('a')
                    else:
                        #cm('b')
                        u.append(v)




                #cm(0,r=1)
                lst0 += u
            else:
                lst0 += sggo(p,'*')
        #kprint(lst0,r=1,t='lst0')
        for l in lst0:
            try:
                skip = skip_f(l)
                #cr(l)
                if not skip and imghdr.what(l) is not None:
                    #cb(l)
                    lst.append(l)
            except:
                pass

    if args.random:
        random.shuffle(lst)
    cg("len(lst) =",len(lst))
    return lst







def hist_L(L):
    rs = []
    for p in L['full_paths']:
        r = 0
        l = len(L['full_paths'][p])
        for n in range(l):
            r += int(L['full_paths'][p][n][0])
        if r > 0:
            r /= (1.0*l)
        rs.append(r)
    figure('hist')
    hist(rs)
    plt.xlabel('rating')
    plt.ylabel('# images')
    plt.title(d2s('rating histogram for',len(rs),'images'))
    raw_enter()
    CA()


def reset_IMAGE_DIC(IMAGE_DIC,L):
    IMAGE_DIC['lst'] = get_list_of_files(L)
    IMAGE_DIC['del_lst'] = []
    IMAGE_DIC['images'] = {}
    IMAGE_DIC['viewed_in_this_session'] = []
    IMAGE_DIC['ctr'] = 0








###########
#
args = get_args()
print(args.slideshow,type(args.slideshow))
kprint(vars(args),r=0)


max_width,max_height = SCREEN_RESOLUTION[0]*args.screen_pro,SCREEN_RESOLUTION[1]*args.screen_pro
min_width,min_height = min(max_width,args.mwidth),min(max_height,args.mheight)

save_timer = Timer(60)
slideshow_timer = Timer(10)
start_timer = Timer()
L = setup_L()

save_L(L)


if args.cmd_lines:
    print_command_lines(L)

    sys.exit()

if args.hist:
    hist_L(L)

g = zeros((intr(max_height*1.),intr(max_width*1.),3),np.uint8)


change = False

if args.slideshow:
    clp("ctrl-C to exit slideshow",'`--rb')
    time.sleep(0)#3)

IMAGE_DIC = {}
reset_IMAGE_DIC(IMAGE_DIC,L)


threading.Thread(target=read_image_to_IMAGE_DIC,args=(IMAGE_DIC,)).start()

i = 0



def loop_body(i,change,IMAGE_DIC):
    lst = IMAGE_DIC['lst']
    if i < -len(lst):
        i = -len(lst)

    out_strs = []
    out_strs.append(cf(i+1,'of',len(lst),'`--d'))


                    
    p = lst[i]
    assert not(args.view_once and args.view_n)
    max_views = 0
    if args.view_once:
        max_views = 0
    elif args.view_n:
        max_views = args.view_n-1

    if p in IMAGE_DIC['viewed_in_this_session']:
        pass
    
    elif (args.view_once or args.view_n) and p in L['full_paths'] and len(L['full_paths'][p]) > max_views:
        i += 1
        return i,change

    if p not in L['full_paths']:
        L['full_paths'][p] = []
    
    rating = None
    rating_str = '['
    if len(L['full_paths'][p]) > 0:
        a = 0
        for b in L['full_paths'][p]:
            a += int(b[0])
        rating = a / (1.0*len(L['full_paths'][p]))
        for i_ in range(intr(rating)):
            rating_str += '*'

    if (args.add_as > 0 and p not in L['full_paths']) or args.add_as == 0:
        if p not in L['full_paths']:
            L['full_paths'][p] = []
        if args.slideshow:
            delay = int(1000 * args.seconds)
        else:
            delay = 0

        h = cf(fname(p),'`',fname(pname(p)),'`--d')
        out_strs.append(h)
        out_strs.insert(0,cf(rating_str,'`y-b'))
        print(' '.join(out_strs))

        e = load_and_display_img(p,g,IMAGE_DIC,delay)

        if e == 'q':
            IMAGE_DIC['del_lst'] = None
            clp('quitting from loop_body')
            if change:
                save_L(L)
            sys.exit()



        #cy("len(IMAGE_DIC['del_lst']) =",len(IMAGE_DIC['del_lst']),len(IMAGE_DIC['lst']),len(IMAGE_DIC['images']),IMAGE_DIC['ctr'])
        if len(IMAGE_DIC['del_lst']) > 20:
            del IMAGE_DIC['images'][IMAGE_DIC['del_lst'].pop(0)]



    #cm('rating =',rating)
    

    #cy(rating_str)

    if args.slideshow:
        #s = max(args.seconds + args.seconds_std * rndn(),0.1)
        #time.sleep(s)
        __,change = process_getch(p,i,change,e)
        i += 1

    elif args.add_as > 0:
        if p not in L['full_paths']:
            L['full_paths'][p] = []
            L['full_paths'][p].append((args.add_as,int(time.time())))
            #cg(L['full_paths'][p],cg("len(L['full_paths']) =",len(L['full_paths'])))
            change = True
        i += 1

    else:
        i,change = process_getch(p,i,change,e)
        if i == 'quit':
            return i,change

    return i,change








while IMAGE_DIC['ctr'] < len(IMAGE_DIC['lst']):

    if save_timer.check() and change:
        save_L(L)
        save_timer.reset()

    if args.slideshow and slideshow_timer.check():
        reset_IMAGE_DIC(IMAGE_DIC,L)
        i = 0
        slideshow_timer.reset()

    use_exceptions = False
    if use_exceptions:
        try:   

            IMAGE_DIC['ctr'],change = loop_body(IMAGE_DIC['ctr'],change,IMAGE_DIC)
        except KeyboardInterrupt:
            cr('*** KeyboardInterrupt ***')
            IMAGE_DIC['del_lst'] = None
            if change:
                save_L(L)
            sys.exit()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('Exception!')
            print(d2s(exc_type,file_name,exc_tb.tb_lineno))
            IMAGE_DIC['ctr'] += 1
            #raw_enter()
    else:
        IMAGE_DIC['ctr'],change = loop_body(IMAGE_DIC['ctr'],change,IMAGE_DIC)
        if IMAGE_DIC['ctr'] == 'quit':
            IMAGE_DIC['del_lst'] = None
            break
    
    
        



if change:
    save_L(L)
   
time.sleep(0.1) 



cg('Done.')




#EOF



if False: ##### KEEP!!!!
    q="Pictures/Photos Library.photoslibrary/Masters/2020"
    heics=get_list_of_files_recursively(q,'*.HEIC',FILES_ONLY=True,ignore_underscore=False)
    jpgs=get_list_of_files_recursively(q,'*.JPG',FILES_ONLY=True,ignore_underscore=False)
    js,hs = [],[]
    for j in jpgs:
        js.append(fnamene(j))
    for j in heics:
        hs.append(fnamene(j))
    n = 0
    for j in js:
        if j not in hs:
            n += 1
            cg(j,n,int(n/(1.0*len(js))*100),'%')
    raw_enter()
    n = 0
    for j in hs:
        if j not in js:
            n += 1
            cg(j,n,int(n/(1.0*len(js))*100),'%')


if False:
    class Cdat:
        def __init__(self,title=''):
            self._title=title
        def add(self, name, val):
            self.__dict__[name] = val
        def kprint(self):
            kprint(vars(self),title=self._title)

    G = Cdat('G')
    G.add('value_1', 'Just me.')
    G.add('value_2', 1)
    G.add('value_3', {'a':'Just me.',2:'adfadsf'})
    G.kprint()

