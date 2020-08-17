#,a
from k3.utils3 import *

if False:
    estr = """file = "/Users/karlzipser/k3/drafts/kimages/kimages_/navigate_dic.py";code=code = file_to_text(file);exec(code);Q = Dnav(D);Q.nav()"""
    Q = Dnav(D); Q.nav(view_action=open_imgs_with_Preview_action,end_action=quit_Preview,top=top)


def errPrint(s):
    clp(s,'`rwb')


def Dnav(Din,A):
    set_Defaults(
        {
        'view_action':kprint,
        'ViewActionArgs':None,
        'line_print_action':None,
        'LinePrintArgs':None,
        'end_action':None,            
        },
        A
    )


    keylist = []


    def nav():
        clear_screen()
        if A['line_print_action']==None:
            A['line_print_action'] = line_print
        while True:
            w = go()
            if w == 'quit':
                if A['end_action'] is not None:
                    A['end_action']()
                return
            elif type(w) == list:
                if 'keylist' in A['ViewActionArgs']:
                    A['ViewActionArgs']['keylist'] = keylist
                if 'D' in A['ViewActionArgs']:
                    A['ViewActionArgs']['D'] = get()
                A['view_action'](w,**A['ViewActionArgs'])       


    def up():
        if len(keylist) > 0:
            keylist.pop()
        else:
            errPrint('<already at top>')


    def get():
        D = Din
        for k in keylist:
            D = D[k]
        return D

    def line_print(ctr,s,k,D):
        if type(D[k]) == dict:
            c = '`wbb'
        else:
            if type(D[k]) == list:
                c = '`bw-'
            else:
                c = '`r'
        clp( '/'.join(keylist+[k]), '`g-b', s, c, d2n('(',ctr,')') )


    def listing():

        ctr = 0

        options = []

        D = get()

        if type(D) is list:
            return None,D

        if len(keylist) > 0:
            clp('<up> (0)')

        ks = D.keys()

        for k in ks:
            ctr += 1
            s = d2n('n=',len(D[k]))
            options.append(k)


            A['line_print_action'](ctr,s,k,D)


        return options,None


    def go():

        options,action_list = listing()#A['line_print_action'](A['LinePrintArgs'])

        if action_list is not None:
            keylist.pop()
            return action_list

        r = raw_input('> ')

        clear_screen()

        if r == 'q':
            return 'quit'

        elif r == 'a':
            lst = []
            E = get()

            for k in E:
                if type(E[k]) == list:
                    lst += E[k]
            return lst

        elif r == '0':
            up()

        elif str_is_int(r):
            if len(options) > 0:
                r_ = int(r)-1
                if r_ < len(options) and r_ >= 0:
                    keylist.append(options[r_])
                else:
                    errPrint(r+' is out of range')
            else:
                errPrint('no options')
        else:
            errPrint('invalid: ' + qtd(r))

    
    return namedtuple('Dnav_object', 'D keylist nav')(Din,keylist,nav)







top = opjD('Photos/all')
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


if False:
    
    if 'D' not in locals():
        D = get_dictionary_of_Photos()

    Q = Dnav(D,
        A = {
            'view_action':kprint,
            'ViewActionArgs': {
                #'top':None,#top,
                #'keylist':None,
                },
            'line_print_action':None,
            'LinePrintArgs':None,
            'end_action':None,            
        },
    )

    Q.nav()
#,b

    #EOF
