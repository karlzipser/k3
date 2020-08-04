from k3.vis3 import *

def get_args():
    
    import argparse

    par = argparse.ArgumentParser(
        prog='mi',
        description='use mi from command line',
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
        '--raw_enter',
        action='store',
        type=int,
        required=False,
        default=1, 
        help='raw_enter option, 0 or 1',
    )

    aa(
        '--random',
        nargs='?',
        const=True, default=False,
        help="one image at a time",
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
        '--min_rating',
        action='store',
        type=int,
        required=False,
        default=0, 
        help='minmum rating (1-9)',
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
        '--mheight',
        action='store',
        type=int,
        required=False,
        default=400, 
        help='max height',
    )

    aa(
        "--view_once",
        nargs='?',
        const=True, default=False,
        help="don't view image if already rated")

    aa(
        "-o",
        "--one",
        nargs='?',
        const=True, default=False,
        help="one image at a time")

    aa(
        "-d",
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

    lst = get_list_of_files(L)

    kprint(lst,t='lst',r=0)


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
    while i < len(lst):
        if args.min_rating == 0 and timer.check():
            timer.reset()
            so(L,opjh('Logs',fname(__file__)+'.'+str(int(time.time()))+'.log'))
        try:   
            if i < -len(lst):
                i = -len(lst)
            clp(i,'of',len(lst))
            p = lst[i]

            if args.view_once and p in L['full_paths'] and len(L['full_paths']) > 0:
                    clp('saw',p,'skipping it')
                    i += 1
                    continue

            img0, theta = load_image_with_orientation(p)
            img = get_resized_img(img0,max_width*0.9,max_height*0.9,min_width*0.9,min_height*0.9)
            f = fname(p)
            if theta:
                c = '`y'
            else:
                c = '`'
            part1 = cf(fname(p),'`',pname(p),'`--du')
            if shape(img0) == shape(img):
                part2 = cf(shape(img0)[:2],c)
            else:
                part2 = cf(shape(img0)[:2],c,'-->',shape(img)[:2],'`r-b')
            clp(part1,part2)

            g *= 0
            img = place_img_f_in_img_g(0,0,img,g,f_center=True,center_in_g=True)
            cv2.namedWindow(f)
            cv2.moveWindow(f,int((screen_sz[0]-max_width)/2),0)

            k = mci(img,title=f)

            if args.one:
                e = getch()

                if p not in L['full_paths']:
                    L['full_paths'][p] = []

                if str_is_int(e):
                    L['full_paths'][p].append((e,int(time.time())))
                    i += 1

                elif e == 'p':
                    i -= 1

                elif e == ' ':
                    i += 1
            
                elif e in ['q','Q','quit','exit']:
                    break#sys.exit()

                else:
                    clp("unused key",'`rwb')
                CA()

        except KeyboardInterrupt:
            cr('*** KeyboardInterrupt ***')
            sys.exit()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('Exception!')
            print(d2s(exc_type,file_name,exc_tb.tb_lineno))
            i += 1
            raw_enter()


    if not args.one and args.raw_enter:
        raw_enter()

    if args.min_rating == 0:
        so(L,opjh('Logs',fname(__file__)+'.'+str(int(time.time()))+'.log'))





def setup_L():
    try:
        os.system('mkdir -p '+opjh('Logs'))
        f = most_recent_file_in_folder(opjh('Logs'),str_elements=[fname(__file__)])
        L = lo(f)
    except:
        L = {}

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

    if args.min_rating > 0:
        for f in L['full_paths']:
            cy(f,L['full_paths'][f])
            if len(L['full_paths'][f]) > 0:
                try:
                    a = 0
                    for b in L['full_paths'][f]:
                        a += int(b[0])
                    r = a / (1.0*len(L['full_paths'][f]))
                    print(dp(r))                  
                    if r >= args.min_rating:
                        lst.append(f)
                except KeyboardInterrupt:
                    cr('*** KeyboardInterrupt ***')
                    sys.exit()
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print('Exception!')
                    print(d2s(exc_type,file_name,exc_tb.tb_lineno))
                    raw_enter()
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



if __name__ == '__main__':
    main()

#EOF