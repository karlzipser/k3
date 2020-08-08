from k3.vis3 import *



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
        nargs="+",
        default=[],
        help='space-separated list of image files to show',
    )

    aa(
        '--paths',
        nargs="+",
        default=[],
        help='space-separated list of paths',
    )

    aa(
        '--ignore_paths',
        nargs="+",
        default=[],
        help='space-separated list of paths to ignore',
    )

    aa(
        '--change',
        nargs='?',
        const=True, default=False,
        help="allow change",
    )    

    aa(
        '--random',
        nargs='?',
        const=True, default=False,
        help="randomize display order",
    )

    aa(
        '--screen_pro',
        action='store',
        type=float,
        required=False,
        default=0.9, 
        help='proportion of screen to use',
    )

    aa(
        '--topic',
        action='store',
        type=str,
        required=False,
        default='no_name', 
        help='name of topic of images',
    )

    aa(
        '--min_rating',
        action='store',
        type=float,
        required=False,
        default=0, 
        help='minmum rating (1-9) to display',
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
        '--max_rating',
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
        help='max width',
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
        help='max height',
    )

    aa(
        "--hist",
        nargs='?',
        const=True, default=False,
        help="make histogram of ratings")

    aa(
        "--view_once",
        nargs='?',
        const=True, default=False,
        help="don't view image if already rated",
    )


    aa(
        "--slideshow",
        nargs='?',
        const=True, default=False,
        help="slideshow mode",
    )

    aa(
        '--seconds',
        action='store',
        type=float,
        required=False,
        default=1.0, 
        help='display seconds',
    )

    aa(
        '--seconds_std',
        action='store',
        type=float,
        required=False,
        default=0., 
        help='display seconds standard deviation',
    )

    aa(
        "--one",
        nargs='?',
        const=True, default=False,
        help="one image at a time")

    aa(
        "--descend",
        nargs='?',
        const=True, default=False,
        help="descend directories collecting images")

    args = par.parse_args()

    return args



args = get_args()
print(args)






def main():

    L = setup_L()

    if args.hist:
        hist_L(L)

    lst = get_list_of_files(L)

    if using_osx:
        def screen_size():
            from Quartz import CGDisplayBounds
            from Quartz import CGMainDisplayID
            mainMonitor = CGDisplayBounds(CGMainDisplayID())
            return (mainMonitor.size.width, mainMonitor.size.height) 
        screen_sz = screen_size()
    else:
        screen_sz = (800,800)

    max_width,max_height = screen_sz[0]*args.screen_pro,screen_sz[1]*args.screen_pro
    min_width,min_height = min(max_width,args.mwidth),min(max_height,args.mheight)

    g = zeros((intr(max_height*1.),intr(max_width*1.),3),np.uint8)

    i = 0
    timer = Timer(60)

    change = False

    while i < len(lst):
        if timer.check() and change:
            save_L(L)
            timer.reset()
            
        try:   
            if i < -len(lst):
                i = -len(lst)
            clp(i+1,'of',len(lst))
            p = lst[i]
            #print(args.view_once, args.view_n)
            assert not(args.view_once and args.view_n)
            max_views = 0
            if args.view_once:
                max_views = 0
            elif args.view_n:
                max_views = args.view_n-1

            if (args.view_once or args.view_n) and p in L['full_paths'] and len(L['full_paths'][p]) > max_views:
                clp('saw',p,len(L['full_paths'][p]),'times, skipping it')
                i += 1
                continue

            if (args.add_as > 0 and p not in L['full_paths']) or args.add_as == 0:
                img0, theta = load_image_with_orientation(p)
                #if not args.one:
                #    img = img0
                #else:
                img = get_resized_img(img0,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
                f = fname(p)
                if theta:
                    c = '`y'
                else:
                    c = '`'
                part1 = cf(fname(p),'`',pname(p),'`--du')

                if args.one:
                    if shape(img0) == shape(img):
                        part2 = cf(shape(img0)[:2],c)
                    else:
                        part2 = cf(shape(img0)[:2],c,'-->',shape(img)[:2],'`r-b')
                    clp(part1,part2)

                g *= 0
                if args.one:
                    img = place_img_f_in_img_g(0,0,img,g,f_center=True,center_in_g=True)
                cv2.namedWindow(f)
                cv2.moveWindow(f,int((screen_sz[0]-max_width)/2),0)

                k = mci(img,title=f)

            if args.one:

                if args.slideshow:
                    s = max(args.seconds + args.seconds_std * rndn(),0.1)
                    time.sleep(s)
                    i += 1

                elif args.add_as > 0:
                    if p not in L['full_paths']:
                        L['full_paths'][p] = []
                        L['full_paths'][p].append((args.add_as,int(time.time())))
                        kprint(L['full_paths'][p])
                        change = True
                        #time.sleep(0.1)
                    i += 1             
                else:

                    e = getch()

                    if p not in L['full_paths']:
                        L['full_paths'][p] = []

                    if str_is_int(e):
                        if args.change:
                            L['full_paths'][p].append((e,int(time.time())))
                            kprint(L['full_paths'][p])
                            i += 1
                            change = True
                        else:
                            raw_enter('change not allowed')

                    elif e == 'p':
                        print('back',i)
                        i -= 1

                    elif e == ' ':
                        i += 1
                
                    elif e in ['q']:
                        break

                    else:
                        clp("unused key",'`rwb')
                CA()
            else:
                i += 1

        except KeyboardInterrupt:
            cr('*** KeyboardInterrupt ***')
            sys.exit()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('Exception!')
            print(d2s(exc_type,file_name,exc_tb.tb_lineno))
            i += 1
            


    if not args.one:
        raw_enter()

    if change:
        save_L(L)

        



def save_L(L):
    so(L,opjh('Logs',fnamene(__file__),args.topic,d2p(fnamene(__file__),args.topic,str(int(time.time())),'log')))

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

    for q in ['filenames','sys.argv']:
        if q not in L:
            L[q] = []
    q = 'full_paths'
    if q not in L:
        L[q] = {}
    L['sys.argv'].append( (sys.argv,int(time.time()) ))
    return L



def get_list_of_files(L):

    lst = []

    if args.min_rating > 0 or args.max_rating < 10:
        for f in L['full_paths']:
            if len(L['full_paths'][f]) > 0:
                try:
                    a = 0
                    for b in L['full_paths'][f]:
                        a += int(b[0])
                    r = a / (1.0*len(L['full_paths'][f]))
                    #print(dp(r))                  
                    if r >= args.min_rating and r <= args.max_rating:
                        #clp(dp(args.min_rating),r,dp(args.max_rating),'`y')
                        lst.append(f)
                    else:
                        pass#clp(dp(args.min_rating),r,dp(args.max_rating),'`b')
                except KeyboardInterrupt:
                    cr('*** KeyboardInterrupt ***')
                    sys.exit()
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print('Exception!')
                    print(d2s(exc_type,file_name,exc_tb.tb_lineno))

    else:
        import imghdr
        lst += args.files
        lst0 = []
        for p in args.paths:
            if False:
                do_continue = False
                clp(args.ignore_paths,p,r=1)
                for a in args.ignore_paths:
                    print(a,p)
                    if a in p:
                        print('ignoreing path '+p)
                        do_continue = True
                        break
                if do_continue:
                    continue

            if args.descend:
                lst0 += get_list_of_files_recursively(p,'*',FILES_ONLY=True,ignore_underscore=False)
            else:
                lst0 += sggo(p,'*')
        for l in lst0:
            try:
                skip = False
                for a in args.ignore_paths:
                    if a in l:
                        clp('skip',a,l)
                        skip = True
                        break
                if not skip and imghdr.what(l) is not None:
                    lst.append(l)
            except:
                pass


    if args.random:
        random.shuffle(lst)

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
    #print(len(rs))
    raw_enter()
    CA()


if __name__ == '__main__':
    main()

#EOF