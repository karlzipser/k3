#,a

from k3.utils.misc.zprint import *


def dict_access(D,name):

    name = cf('dictionary '+name,'`--u')
    print('name 0',name)
    if '__menu_path__' not in D:
        D['__menu_path__'] = None
    if '__max_depth__' not in D:
        D['__max_depth__'] = 10**3


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
        name=name,
    ):

        def _zprint(z,p,D,t):
            if z:
                if t is None: t = p
                zprint(D,t,max_depth=10**3)

        if p == '':
            p = None

        if m is not None:
            assert_as(p is None,"p is None")
            p = D['__menu_path__']
            m = None

        if ud in [-1,1]:
            assert(p is None and e is None and prune is False and m is None)

        #print('name 0',name)

        if ud == -1:
            assert_as('__menu_path__' in D,"'__menu_path__' in D")
            D['__menu_path__'] = pname_(D['__menu_path__'])
                #cm('zp0')
            if D['__menu_path__'] is None:
                #cg(1)
                n = '' #name
                #cg(n)
            else:
                #cg(2)
                n = D['__menu_path__']
            _zprint(1,None,o( D['__menu_path__'] ),name+'/'+n)

        elif ud == 1:
            n = D['__menu_path__']
            O = o( D['__menu_path__'] )
            if type(O) is dict and len(O) > 0:# and not( len(O)==1 and not (type(O[kys(O)[0]]) is dict and len(O[kys(O)[0]]) == 0)):
                #cg(type(O),len(O),O)
            #if type(O) is dict:
                if len(O) > 1:
                    k = select_from_list( kys(O))
                    clear_screen()
                else:
                    k = kys(O)[0]
                if D['__menu_path__'] is None:
                    D['__menu_path__'] = k + '/'
                    n = ''
                else:
                    D['__menu_path__'] = D['__menu_path__'] + k + '/'
                    n = D['__menu_path__']
                #cm('zp1')
            _zprint(1,None,o( D['__menu_path__'] ),name+'/'+n)

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
                #cm('zp2')
                _zprint(z,p,D,'t')
            else:
                #cm('zp3')
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
            #cg(key_list)
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
    return lst[i]

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

clear_screen()
oD(z=1)
c = None
while c != 'q':
    c = input_from_range(choices=[1,-1,'q','m'])
    if c == 'm':
        D['__max_depth__']=1+input_int_in_range(0,99999,'>>> ')
    #cy(1)
    clear_screen()
    #cy(2)
    if c is None:
        continue
    
    #try:
    oD(ud=c)
    #except:
    #    print('oops!')
#EOF

#,b



