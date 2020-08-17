from k3.vis3 import *

import k3.drafts.kimages.kimages_.navigate_dic as navigate_dic

top = opjD('Photos/all')




def nav():

    D = get_dictionary_of_Photos()

    Q = navigate_dic.Dnav(D)

    Q.nav(
        {
        'action':kprint,
        'ActionArgs': {
            'top':top,
            'keylist':None,
            },
        'ListingAction':None,
        'ListingArgs':None,
        'end_action':None,            
        },
        #action=open_imgs_with_Preview_action,

        #end_action=quit_Preview,

        )


def open_imgs_with_Preview_action(f,keylist=[],top=[]):
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




if True:


    def line_print_(ctr,s,k,D):
        cm(ctr,s,k,D[k])
   
    if 'D' not in locals():
        D = get_dictionary_of_Photos()

    Q = navigate_dic.Dnav(
        D,
        A = {
            'view_action':open_imgs_with_Preview_action,
            'ViewActionArgs': {
                'top':top,
                'keylist':None,
            },
            'line_print_action':None,#line_print_,
            'LinePrintArgs':None,
            'end_action':quit_Preview,            
        },
    )

    Q.nav()


#EOF

