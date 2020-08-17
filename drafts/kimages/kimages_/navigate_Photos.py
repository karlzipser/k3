from k3.vis3 import *


def open_imgs_with_Preview_action(f,keylist=[],top=[]):
    h = []
    kprint(f)
    for g in f:
        g = opj(pname(g),fname(g).split('|')[-1])
        h.append(opj(top,'/'.join(keylist),g))
    quit_Preview()
    open_imgs_with_Preview(h)
    #time.sleep(5)
    #os_system("osascript Desktop/bring_terminal_to_front.scpt",e=1)


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


if False:
    ff = get_photo_dirs()

    mm = sggo(f,'.meta','*')
    dirs = []
    files = []
    for m in mm:
        if os.path.isdir(m):
            dirs.append(m)
        else:
            files.append(m)


P = {
    'min_rating':0,
    'max_rating':10,
}

def get_dictionary_of_Photos():
    D = {}
    years = []
    top = opjD('Photos/all')
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
    #kprint(D)
    return D

#EOF