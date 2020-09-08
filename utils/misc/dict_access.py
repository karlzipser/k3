#,a

from k3.utils.misc.zprint import *


def dict_access(D,name):

    name = cf('dictionary '+name,'`--u')
    print('name 0',name)
    if '__meta__' not in D:
        D['__meta__'] = {
            'menu_path':None,
            'max_depth':10**6,
            'ignore_underscore':False,
        }

    def o(
        p=None,
        e=None,
        create_missing_paths=True,
        report_path_creation=True,
        deepcopy=True,
        prune=False,
        z=False,
        t=None,
        ud=0,
        m=None,
        D=D,
        Meta=D['__meta__'],
        name=name,
    ):

        def _zprint(z,p,D,t):
            if z:
                if t is None:
                    t = p
                zprint(D,t,max_depth=Meta['max_depth']+1)

        if p == '':
            p = None

        if m is not None:
            assert_as(p is None,"p is None")
            p = Meta['menu_path']
            m = None

        if ud in [-1,1]:
            assert(p is None and e is None and prune is False and m is None)

        n = None
        if ud == 'u':
            assert_as('menu_path' in Meta,"'menu_path' in D")
            Meta['menu_path'] = pname_(Meta['menu_path'])

            if Meta['menu_path'] is None:
                n = ''

            else:

                n = Meta['menu_path']

        elif ud == 'd':
            n = Meta['menu_path']
            O = o( Meta['menu_path'] )
            if type(O) is dict and len(O) > 0:
                if len(O) > 1:
                    k = None
                    while k is None:
                        k = select_from_list( kys(O))
                    clear_screen()
                else:
                    k = kys(O)[0]
                if Meta['menu_path'] is None:
                    Meta['menu_path'] = k + '/'
                    n = ''
                else:
                    Meta['menu_path'] = Meta['menu_path'] + k + '/'
                    n = Meta['menu_path']

        if ud in ['u','d','-']:
            if n is None:
                if Meta['menu_path'] is None:
                    n = ''
                else:
                    n = Meta['menu_path']
            _zprint(1,None,o( Meta['menu_path'] ),name+'/'+n)

        assert_as(D is not None,"D is not None")

        assert_as(p is None or has_form_of_path(p),d2s(qtd(p),"is None or has_form_of_path(",qtd(p),")"))

        if p is not None:
            key_list = p[:-1].split('/')


        if e == None:

            if p is not None:

                for i in rlen(key_list):
                    k = key_list[i]
                    if prune and i == len(key_list)-1:
                        print(key_list)
                        del D[k]
                        break
                    
                    assert_as( k in D, d2s("k in D? No,",qtd(k),"not in",D))
                    D = D[k]
                _zprint(z,p,D,'t')
            else:
                _zprint(z,p,D,'')

            return D 
        else:
            assert_as(not(prune),"not(prune)")
            if deepcopy:
                e = copy.deepcopy(e)
            assert_as(p is not None,"p is not None")
            for k in key_list[:-1]:
                if k not in D:
                    if create_missing_paths:
                        if report_path_creation:
                            print( d2s('creating',qtd(k)) )
                        D[k] = {}
                D = D[k]
            k = key_list[-1]
            D[k] = e
            _zprint(z,p,D,t)
            return e
    return o


def has_form_of_path(s):
    if type(s) == str:
        if len(s) > 1:
            if s[0] != '/':
                if s[-1] == '/':
                    return True
    return False 



def pname_(path):
    if path == None:
        return None
    assert has_form_of_path(path)
    path = pname( path[:-1] ) + '/'
    if path in ['/','']:
        path = None
    else:
        assert has_form_of_path(path)
    return path


def input_int(s='> '):
    c = input(s)
    if str_is_int(c):
        return int(c)
    else:
        return None

def input_from_range(s='> ',choices=[]):
    c = input(s)
    if str_is_int(c):
        c = int(c)
    if c in choices:
        return c
    else:
        return None

def input_int_in_range(a,b,s):
    c = input_int(s)
    if c is None or c < a or c > b:
        return None
    else:
        return c

def select_from_list(lst,ignore_underscore=True):
    ctr = 0
    for i in rlen(lst):
        if ignore_underscore and lst[i][0] != '_':
            clp('    ',i,') ',lst[i],s0='')
            ctr += 1
    if ctr > 1:
        i = input_int_in_range(0,len(lst)-1,'>> ')
    else:
        i = 0
    if i is None:
        return None
    return lst[i]

def files_to_dict(path,D={}):
    D['.'] = []

    fs = sggo(path,'*')
    for f in fs:
        if not os.path.isdir(f):
            D['.'].append(fname(f))
        else:
            D[fname(f)] = files_to_dict(f,{})
    return D






if __name__ == '__main__':
 
    code = """

clear_screen()

if '__file__' in locals(): eg(__file__)

import copy

D = {}
oD = dict_access(D,'D')
oD('a/b/c/d/e/',e=1,z=1)

E = {}
oE = dict_access(E,'E')
oE('a/b/c/d/e/',e=2,z=1)

oD(z=1)
oE(z=1)

oD('Y/',e=oE('a/'))
oD(z=1)  
oD('a/b/c/d/',prune=1)
oD(z=1)

    """

    for c in code.split('\n'):
        if not c.isspace():
            clp(c,'`--u')
            exec(c)

    D=files_to_dict(opjh('Desktops_older'),D={})
    oD = dict_access(D,'Desktops_older')

    clear_screen()
    oD(ud='-')
    c = None
    while c != 'q':
        c = input_from_range(choices=['u','d','q','m'])
        if c == 'm':
            i = input_int_in_range(0,10*10,d2n('max depth (',D['__meta__']['max_depth'],') >>> '))
            if type(i) is int:
                D['__meta__']['max_depth'] = i
            clear_screen()
            oD(ud='-')
            continue

        if c is None:
            cm(qtd(c),'not recognized.')
            oD(ud='-')
            continue
        
        #try:
        oD(ud=c)
        #except:
        #    print('oops!')
#EOF

#,b



