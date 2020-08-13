
from k3.vis3 import *

from collections import namedtuple
TimerC = namedtuple('TimerC', 'save slideshow start')
timer = TimerC
timer.save = Timer(60)
timer.slideshow = Timer(10)
timer.start = Timer()

min_width,min_height,max_width,max_height,g = None,None,None,None,None
#cr( min_width,min_height,max_width,max_height )


def read_image_to_IMAGE_DIC(IMAGE_DIC):

    while True:

        if IMAGE_DIC['del_lst'] is None:
            break

        if len(IMAGE_DIC['lst']) > 0 and len(IMAGE_DIC['lst']) < IMAGE_DIC['ctr'] and len(IMAGE_DIC['images']) <= ( 100 - len(IMAGE_DIC['del_lst']) ):
            #cm(len(IMAGE_DIC['lst']),IMAGE_DIC['ctr'])
            p = IMAGE_DIC['lst'][ IMAGE_DIC['ctr'] ]
            IMAGE_DIC['ctr'] += 1
            img0, theta = load_image_with_orientation(p)
            img = get_resized_img(img0,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
            IMAGE_DIC['images'][p] = img,shape(img0),theta

        else:
            time.sleep(0.1)
                        
    print("exiting read_image_to_IMAGE_DIC")

    

def load_and_display_img(p,IMAGE_DIC,delay,args):

    #cb( min_width,min_height,max_width,max_height )

    if p not in IMAGE_DIC['images']:
        #cb(fname(p),"not in IMAGE_DIC, loadiing.")
        cb("< loading delay >")
        img0, theta = load_image_with_orientation(p)
        img = get_resized_img(img0,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
        IMAGE_DIC['images'][p] = img,shape(img0),theta
        img0_shape = shape(img0)
    else:
        img,img0_shape,theta = IMAGE_DIC['images'][p]

    if p not in IMAGE_DIC['viewed_in_this_session']:
        IMAGE_DIC['viewed_in_this_session'].append(p)
        #cm("IMAGE_DIC['viewed_in_this_session'].append(p)")
    else:
        pass
        #cm("don't IMAGE_DIC['viewed_in_this_session'].append(p)")
    #kprint(IMAGE_DIC['viewed_in_this_session'])

    if p not in IMAGE_DIC['del_lst']:
        IMAGE_DIC['del_lst'].append(p)

    #cm(type(img),type(g))
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
        #print(e)
    else:
        e = ''

    return e

KEYS = {
    'save_copy_keys':['/'],
    'clear_keys':   ['-'],
    'back_keys':    ['<','['],
    'forward_keys': ['>',']',' ','<space bar>'],
    'quit_keys':    ['`','<tilde key>',';'],
    'not_yet_viewed_count_keys':    ['='],
    'help_keys':    [','],
}
kprint(KEYS,title='KEYS')





def images_not_yet_viewed_count(L,IMAGE_DIC):
    c = 0
    for p in IMAGE_DIC['lst']:
        if p not in L['full_paths']:
            c += 1
    clp(c,"of images",'('+str(intr(100*c/len(IMAGE_DIC['lst'])))+'%)',len(IMAGE_DIC['lst']),"not viewed yet")


def process_getch(p,i,change,e,L,IMAGE_DIC,args):

    #kprint(L['full_paths'],title="L['full_paths']")

    #cm(args.slideshow)
    if len(e) == 0:
        pass

    elif e in KEYS['save_copy_keys']:
        p_safe = get_safe_name(p.replace('/','__'),safe_chars=['.','-'])
        s = d2s("cp",'\"'+p+'\"',opjD(p_safe))
        os_system(s,e=1)

    elif str_is_int(e):
        if args.change:
            L['full_paths'][p].append((e,int(time.time())))

            i += 1
            change = True
        else:
            raw_enter('change not allowed')

    elif e in KEYS['clear_keys']:
        if args.change:
            L['full_paths'][p] = []
            clp('Cleared',fname(p),'`ybb')

    elif e in KEYS['back_keys']:
        cm("elif e in KEYS['back_keys']:")
        i -= 1

    elif e in KEYS['forward_keys']:
        i += 1

    elif e in KEYS['not_yet_viewed_count_keys']:
        images_not_yet_viewed_count(L,IMAGE_DIC)

    elif e in KEYS['help_keys']:
        kprint(KEYS,title='KEYS')

    elif e in KEYS['quit_keys']:
        return 'quit',change

    else:
        clp('\''+e+'\'',"is and unused key",'`rwb')

    return i,change




def save_L(L,args):
    file_path = opjh('Logs',args.project_name,args.topic,d2p(args.project_name,args.topic,str(int(time.time())),'log'))
    latest_path = opj(pname(file_path),'latest.pkl')
    so(L,file_path)
    os.system(d2s('rm',latest_path))
    os.system(d2s('ln -s',file_path,latest_path))


def setup_L(args):

    global min_width,min_height,max_width,max_height,g
    max_width,max_height = int(SCREEN_RESOLUTION[0]*args.screen_pro), int(SCREEN_RESOLUTION[1]*args.screen_pro)
    min_width,min_height = int(min(max_width,args.mwidth)), int(min(max_height,args.mheight))
    g = zeros((intr(max_height*1.), intr(max_width*1.),3),np.uint8)
    #cg( min_width,min_height,max_width,max_height )

    try:
        os.system('mkdir -p '+opjh('Logs',args.project_name,args.topic))
        f = most_recent_file_in_folder(opjh('Logs',args.project_name,args.topic),str_elements=[args.topic,'.log.pkl']) #args.project_name])
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



def _skip_f(f,args,verbose=True):
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



def _get_list_of_files(L,args):

    lst = []

    if args.slideshow or args.min_rating > 0 or args.max_rating < 10 or args.progressive_range:

        if len(L['full_paths']) == 0:
            clp("warning, len(L['full_paths']) == 0",
                "with args.slideshow or args.min_rating > 0 or args.max_rating < 10",
                "or args.progressive_range True",'`wrb')

        for f in L['full_paths']:

            if _skip_f(f,args):
                continue

            if len(L['full_paths'][f]) > 0:
                try:
                    a = 0
                    for b in L['full_paths'][f]:
                        a += int(b[0])
                    r = a / (1.0*len(L['full_paths'][f]))

                    if args.progressive_range:
                        if timer.start.time() < 30:
                            if r >= 4 and r <= 5:
                                lst.append(f)
                        elif timer.start.time() < 60:
                            if r >= 4 and r <= 6:
                                lst.append(f)
                        elif timer.start.time() < 90:
                            if r >= 5 and r <= 7:
                                lst.append(f)
                        elif timer.start.time() < 120:
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
        if len(args.files) + len(args.paths) == 0:
            clp('Warning, no files or paths specified, use --files and/or --paths cmd line args with --descend option.','`wrb',r=1)

        import imghdr
        lst += args.files
        lst0 = []
        for p in args.paths:
            #cy(p,r=1)
            if args.descend:
                #cg('here!',r=1)
                q = get_list_of_files_recursively(p,'*',FILES_ONLY=True,ignore_underscore=False)
                if len(q) == 0:
                    clp('Warning, no files or paths specified, use --files and/or --paths cmd line args with --descend option.','`wrb',r=1)
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
            if l[0] == '/':
                l = l[1:]
            try:
                skip = _skip_f(l,args)
                cr(l)
                if not skip and imghdr.what(l) is not None:
                    cb(l)
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


def reset_IMAGE_DIC(IMAGE_DIC,L,args):
    IMAGE_DIC['lst'] = _get_list_of_files(L,args)
    IMAGE_DIC['del_lst'] = []
    IMAGE_DIC['images'] = {}
    if 'viewed_in_this_session' not in IMAGE_DIC:
        IMAGE_DIC['viewed_in_this_session'] = []
        #cm("IMAGE_DIC['viewed_in_this_session'] = []")
    IMAGE_DIC['ctr'] = 0

