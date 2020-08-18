from k3.vis3 import *

#import k3.drafts.kimages.kimages_.navigate_dic as navigate_dic

top = opjD('Photos/all')





def open_imgs_with_Preview_action(f,Args=None,MiniMenu=None):
    #kprint(Args,'Args0',r=1)
    #kprint(MiniMenu,'B0',r=1)
    keylist = Args['keylist']
    top = Args['top']
    True
    h = []
    kprint(f,'open_imgs_with_Preview_action')
    for g in f:
        g = opj(pname(g),fname(g).split('|')[-1])
        h.append(opj(top,'/'.join(keylist),g))
    quit_Preview()
    open_imgs_with_Preview(h)


def rating_from_filename(f):
    
    if 'ratings=' not in f:
        return None

    f = f.split('|')[0]

    f = f.split('ratings=')[-1]

    l = f.split(',')

    c = 0
    
    for a in l:
        
        c += int(a)

    c /= len(l)

    return c


def get_dictionary_of_Photos():
    D = {}
    years = []
    a = sggo(top,'*')
    for b in a:
        years.append(b.split('/')[-1])
    for y in years:
        D[y] = {}
    for y in years:
        months = []
        c = sggo(top,y,'*')
        for d in c:
            months.append(d.split('/')[-1])
        for m in months:
            D[y][m] = {}
            days = []
            e = sggo(top,y,m,'*')
            for f in e:
                days.append(f.split('/')[-1])
            for g in days:
                h = sggo(top,y,m,g,'.meta/*')
                D[y][m][g] = {}
                D[y][m][g]['<unsorted>'] = []
                for j in h:
                    if os.path.isfile(j):
                        D[y][m][g]['<unsorted>'].append(j.split('/')[-1])
                    else:
                        D[y][m][g][fname(j)] = []
                        k = sggo(j,'*.jpeg')
                        for u in k:
                            D[y][m][g][fname(j)].append(u.split('/')[-1])
    return D


# 2020/05/06/<unsorted> n=13 (1)

def ratings_filter(w,Args=None,MiniMenu=None):
    #kprint(Args,'Args',r=1)
    #kprint(MiniMenu,'MiniMenu',r=1)
    rmin = MiniMenu['rmin']
    rmax = MiniMenu['rmax']
    show_unrated = MiniMenu['show_unrated']
    True
    kprint(MiniMenu)
    print(rmin,rmax,show_unrated)               
    _lst = []
    for l in w:
        c = rating_from_filename(l)
        #cm( l,c,c is None , show_unrated,c >= rmin and c <= rmax)
        if c is None and not show_unrated:
            continue
        if (c is None and show_unrated) or (c >= rmin and c <= rmax):
            _lst.append(l)
    return _lst
                









if True:


    def line_print_(ctr,s,k,D):
        cm(ctr,s,k,D[k])
   
    if 'D' not in locals():
        D = get_dictionary_of_Photos()

    Q = Navigate_dictionary(
        D,
        A = {
            'view':{
                'action':open_imgs_with_Preview_action,
                'Args':{
                    'top':top,
                    'keylist':None,
                },
            },
            'end':{
                'action':quit_Preview,
                'Args':None,
            },
            'filter':{
                'action':ratings_filter,
                'Args':None, 
            },
            'mini_menu':{
                'action':mini_menu,
                'Args': {
                    'menu_tuple':(
                        ('rmin',(0,10,0)),
                        ('rmax',(0,10,10)),
                        ('show_unrated',(True,False,True)),
                    ),
                },
            },
        },
    )

    Q.nav()


#EOF










