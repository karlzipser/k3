
from kimages_.utils import *


def body(i,i_prev,change,IMAGE_DIC,L,args):

    #cm(i,i_prev)

    i_save = i

    lst = IMAGE_DIC['lst']

    if i < -len(lst):
        i = -len(lst)

    out_strs = []
    out_strs.append(cf(i+1,'of',len(lst),'`--d'))

    p = lst[i]

    max_views = 0

    if args.view_once:
        max_views = 0

    elif args.view_n:
        max_views = args.view_n-1

    if p in IMAGE_DIC['viewed_in_this_session']:
        #cm("if p in IMAGE_DIC['viewed_in_this_session']")
        pass
    
    elif (args.view_once or args.view_n) and p in L['full_paths'] and len(L['full_paths'][p]) > max_views:
        #cm("IS THIS THE PROBLEM?")
        if i > i_prev:
            i += 1
        elif i < i_prev:
            i -= 1
        else:
            assert(False)
        return i,i_save,change

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

        e = load_and_display_img(p,IMAGE_DIC,delay,args)

        if e in KEYS['quit_keys']:
            IMAGE_DIC['del_lst'] = None
            clp('quitting from loop_body')
            if change:
                save_L(L,args)
            sys.exit()

        if len(IMAGE_DIC['del_lst']) > 20:
            del IMAGE_DIC['images'][IMAGE_DIC['del_lst'].pop(0)]


    if args.slideshow:

        __,change = process_getch(p,i,change,e,L,IMAGE_DIC,args)
        i += 1

    elif args.add_as > 0:
        if p not in L['full_paths']:
            L['full_paths'][p] = []
            L['full_paths'][p].append((args.add_as,int(time.time())))
            change = True
        i += 1

    else:
        i,change = process_getch(p,i,change,e,L,IMAGE_DIC,args)
        ##cm(i)
        if i == 'quit':
            return i,i_save,change

    return i,i_save,change

