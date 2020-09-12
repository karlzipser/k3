# ,a

from k3.utils.misc.zprint import *
from k3.utils.misc.clipcode import *


def dict_access(D,name):

    name = cf(name,'`--u')
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
        up_down=None,
        use_meta_path=False,
        D=D,
        Meta=D['__meta__'],
        name=name,
    ):


        def _zprint(z=0,p=None,D=None,t=None,do_return=0,do_print=1):
            if z:
                if t is None:
                    t = p
                if Meta['menu_path'] is None:
                    mp = ''
                else:
                    mp = Meta['menu_path']
                return zprint(
                        D,
                        t=name+'/'+mp,
                        max_depth=Meta['max_depth']+1,
                        do_return=do_return,
                        do_print=do_print
                        )
        if p == '':
            p = None

        if use_meta_path:
            assert_as(p is None,"p is None")
            p = Meta['menu_path']


        if up_down in ['u','d','-']:

            assert(p is None and e is None \
                and prune is False and use_meta_path is False)

            if up_down == 'u':
                assert_as('menu_path' in Meta,"'menu_path' in D")
                Meta['menu_path'] = pname_(Meta['menu_path'])

            elif up_down == 'd':
                O = o( Meta['menu_path'] )
                if type(O) is dict and len(O) > 0:
                    if len(O) > 1:
                        k = None
                        while k is None:
                            k = select_from_list( kys(O))
                    else:
                        k = kys(O)[0]
                    if Meta['menu_path'] is None:
                        Meta['menu_path'] = k + '/'
                    else:
                        Meta['menu_path'] = Meta['menu_path'] + k + '/'

            zD,print_lines = _zprint(
                z=1,
                p=None,
                D=o( Meta['menu_path'] ),
                do_return=1,
                do_print=0
            )

            dpath_prev = None
            indx_prev = None

            U = {}
            ctr = 0

            for i in range(1,len(print_lines)):
                j = i-1

                d = zD[j]

                n = ''
                n_show = ''  

                indx = None
                d = d[1:]
                if len(d) > 0 and type(d[-1]) is tuple and len(d[-1]) == 1:
                    indx = d[-1][0]
                    d = d[:-1]

                dpath = pa(d)
                if dpath == '/':
                    dpath = ''
                if Meta['menu_path'] is None:
                    mp = ''
                else:
                    mp = Meta['menu_path']
                dpath = mp + dpath
                U[ctr] = {'path':dpath,'lst_indx':indx}
                
                if d2s(dpath,indx) != d2s(dpath_prev,indx_prev):
                    ctr_show = cf(ctr,'`--d')
                    ctr += 1
                else:
                    ctr_show = ''
                dpath_prev = dpath
                indx_prev = indx
                print(print_lines[i],ctr_show)


            return U,print_lines


        assert_as(D is not None,"D is not None")

        assert_as(
            p is None or has_form_of_path(p), d2s(qtd(p),
            "is None or has_form_of_path(",qtd(p),")"))


        if p is not None:
            key_list = p[:-1].split('/')


        if e == None:
            if p is not None:
                for i in rlen(key_list):
                    k = key_list[i]
                    if prune and i == len(key_list)-1:
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




def count_nodes(D):
    if type(D) is not dict:
        return 1
    n = 1    
    ks = kys(D)
    for k in ks:
        n += count_nodes(D[k])
    return n

def condense_dict(D):
    if type(D) is not dict:
        return D
    ks = kys(D)
    if len(ks) == 1:
        return condense_dict(D[ks[0]])
    for k in ks:
        D[k] = condense_dict(D[k])
    return D


            


def __has_form_of_path(s):
    if type(s) == str:
        if len(s) > 1:
            if s[0] != '/':
                if s[-1] == '/':
                    return True
    return False 

_re = r'^([\s|\w|_|\d|\.|\-|`|~|\!|@|#|\$|%|\^|&|*|\(|\)|\[|\]|\{|\}]+/)+$'
def has_form_of_path(s):
    if type(s) == str:
        if re.match(
            _re, s ):
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


def pa(lst):
    return d2f('/',*lst)+'/'




if not interactive() and __name__ == '__main__':


    if '__file__' in locals(): eg(__file__)


    raw_code = get_code_snippet_(__file__,start='#,---a',stop='#,---b')
    v = raw_code.split('\n')[1:]
    q = []
    indent_spaces = 4
    for r in v:
        q.append(r[indent_spaces:])
    raw_code = '\n'.join( q )
    
    #import matplotlib.pyplot as plt
    for c in raw_code.split('#.'):
        if not c.isspace():
            clp(c,'`--r')
            #clp(c[indent_spaces:],indent_spaces,'`---')
            exec(c)
            #plt.pause(3)
            time.sleep(3)

    if False:
        D=files_to_dict(opjh('Desktops_older/Desktop_30Jan19_10h14m01s'),D={})
        D = condense_dict(D)
        oD = dict_access(D,'Desktops_older/Desktop_30Jan19_10h14m01s/')

        #clear_screen()
        oD(up_down='-')
        c = None
        U = {}
        while True:
            c = input('-> ')#_from_choices(choices=['u','d','q','m'])

            if c == 'q':
                break

            if c is None:
                c = '-'

            if c == 'm':
                i = input_int_in_range(
                    0,
                    10*10,
                    d2n('max depth (',D['__meta__']['max_depth'],') >>> ')
                )
                if type(i) is int:
                    D['__meta__']['max_depth'] = i

                oD(up_down='-')
                continue
            
            if True:

                if c in ['u','d']:
                    cc = c
                else:
                    cc = '-'
                U,print_lines = oD(up_down=cc)

                if str_is_int(c.split(' ')[0]):
                    i = int(c.split(' ')[0])
                    if i in U:
                        p = U[i]['path']
                        oD('__meta__/menu_path/',e=p)
                        if False:
                            clp(p,'`ybb') #oD('__meta__/menu_path/'),U[i]['path'],p,'`yb')
                            if U[i]['lst_indx'] is None:
                                cy('out:',oD(p))
                            else:
                                cg('out:',oD(p)[U[i]['lst_indx']])
            
                    oD(up_down='-')
                    if U[i]['lst_indx'] is None:
                        cy('out:',oD(p))
                    else:
                        cg('out:',oD(p)[U[i]['lst_indx']])
                    if len(c.split(' ')[0]) > 1:
                        if c.split(' ')[1] == 'o':
                            cg('open',opjh('Desktops_older/Desktop_30Jan19_10h14m01s',p),r=1)


            else:#except:
                print('oops!')


if False:
#############################
#,---a
    D = {} #.
    oD = dict_access(D,'D') #.
    oD('a/b/c/d/e/',e=['x','y','z'],z=1) #.

    E = {} #.
    oE = dict_access(E,'E') #.
    oE('a/b/c/d/e/',e=2,z=1) #.

    oD(z=1)
    oE(z=1)

    oD('Y/',e=oE('a/'))#.
    oD(z=1)  #.
    oD('a/b/c/d/',prune=1)
    oD(z=1) #.
    print(oD('a/b/'))

#,---b
#############################

#EOF

# ,b



