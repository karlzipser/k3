# ,a

from k3.utils.misc.zprint import *
from k3.utils.misc.clipcode import *

def dict_access(D,name):

    name = cf(name,'`--u')
    print('name 0',name)
    if '__meta__' not in D:
        D['__meta__'] = {
            'menu_path':None,
            'max_depth':10**6,
            'ignore_underscore':False,
        }

    def _____zprint(z,p,D_,t,do_return=0,do_print=1):

        if z:
            if t is None:
                t = p
            if do_return:
                return zprint(D_,max_depth=D['__meta__']['max_depth']+1,do_return=do_return,do_print=do_print)
            else:
                return zprint(D_,t,max_depth=D['__meta__']['max_depth']+1,do_return=do_return,do_print=do_print)

    def o(
        p=None,
        e=None,
        create_missing_paths=True,
        report_path_creation=True,
        deepcopy=True,
        prune=False,
        z=False,
        t=None,
        ud=None,
        m=None,
        D=D,
        Meta=D['__meta__'],
        name=name,
    ):


        def _zprint(z,p,D,t,do_return=0,do_print=1):

            if z:
                if t is None:
                    t = p
                if do_return:
                    return zprint(D,max_depth=Meta['max_depth']+1,do_return=do_return,do_print=do_print)
                else:
                    return zprint(D,t,max_depth=Meta['max_depth']+1,do_return=do_return,do_print=do_print)



        if p == '':
            p = None

        if m is not None:
            assert_as(p is None,"p is None")
            p = Meta['menu_path']
            m = None





        if ud in ['u','d','-']:

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
                    else:
                        k = kys(O)[0]
                    if Meta['menu_path'] is None:
                        Meta['menu_path'] = k + '/'
                        n = ''
                    else:
                        Meta['menu_path'] = Meta['menu_path'] + k + '/'
                        n = Meta['menu_path']

            if n is None:
                if Meta['menu_path'] is None:
                    n = ''
                else:
                    n = Meta['menu_path']

            zD,print_lines = _zprint(z=1,p=None,D=o( Meta['menu_path'] ),t=name+'/'+n,do_return=1,do_print=0)

            n_prev = None

            U = {}
            ctr = 0
            for i in range(1,len(print_lines)):
                j = i-1

                d = zD[j]
                if len(d) > 0 and type(d[-1]) is tuple and len(d[-1]) == 1:
                    indx = d[-1][0]
                else:
                    indx = ''
                n = ''
                n_show = ''
                try:
                    n = pa(d)
                except:
                    pass
                if n != n_prev:
                    n_prev = n
                    n_show = n.split('(')[0]
                    s = str(i)
                else:
                    s = ''
                while len(s) < 4:
                    s = s+' '
                if n_show == '':
                    indx = ''
                if len(n_show.split('/')) == 2:
                    n_show = '/'
                else:
                    n_show = '/'.join(n_show.split('/')[1:])

                if len(n_show) > 0:
                    if n_show[-1] != '/':
                        n_show = n_show+'/'
                else:
                    n_show = ''

                if False:
                    print(s,print_lines[i],cf(n_show,'`b',indx,'`g'))

                if n_show != '':
                    if Meta['menu_path'] is None:
                        mp = ''
                    else:
                        mp = Meta['menu_path']
                    if type(indx) is int:
                        U[ctr] = {'path':mp+n_show,'lst_indx':indx}
                    else:
                        U[ctr] = {'path':mp+n_show,'lst_indx':None}
                    ctr_show = cf(ctr,'`--d')
                    U_ctr_show = U[ctr]
                    ctr += 1
                else:
                    ctr_show = ''
                    U_ctr_show = ''
                
                print(print_lines[i],ctr_show)

            if False:
                i = input_int('>>> ')
                if i in U:
                    if U[i][1] is None:
                        print(i,U[i][0])
                        cm(oD(U[i][0]))
                    else:
                        print(i,U[i][0],U[i][1])
                        cy(oD('__meta__/menu_path/'))
                        if oD('__meta__/menu_path/'):

                            p = oD('__meta__/menu_path/')+ U[i][0]
                        else:
                            p = U[i][0]
                        cr(oD(p)[U[i][1]])

                return U[i],print_lines

            return U,print_lines





        assert_as(D is not None,"D is not None")

        assert_as(p is None or has_form_of_path(p), d2s(qtd(p),"is None or has_form_of_path(",qtd(p),")"))

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


def pa(lst):
    return d2f('/',*lst)+'/'





if __name__ == '__main__':


    if '__file__' in locals(): eg(__file__)


    raw_code = get_code_snippet_(__file__,start='#,---a',stop='#,---b')
    v = raw_code.split('\n')[1:]
    q = []
    indent_spaces = 4
    for r in v:
        q.append(r[indent_spaces:])
    raw_code = '\n'.join( q )
    
    
    for c in raw_code.split('#.'):
        if not c.isspace():
            clp(c,'`--r')
            #clp(c[indent_spaces:],indent_spaces,'`---')
            exec(c)

    if True:
        #D=files_to_dict(opjh('Desktops_older/Desktop_30Jan19_10h14m01s'),D={})
        #oD = dict_access(D,'Desktops_older/Desktop_30Jan19_10h14m01s/')

        clear_screen()
        #oD(ud='-')
        c = None
        U = {}
        while True:
            c = input('>>>>')#_from_choices(choices=['u','d','q','m'])

            if c == 'q':
                break

            if c is None:
                c = '-'

            if c == 'm':
                i = input_int_in_range(0,10*10,d2n('max depth (',D['__meta__']['max_depth'],') >>> '))
                if type(i) is int:
                    D['__meta__']['max_depth'] = i
                clear_screen()
                oD(ud='-')
                continue
            
            if True:#try:
                assert_as(c in ['u','d','-'] or str_is_int(c),d2s(c,"in ['u','d','-'] or str_is_int(c)"))
                cr(c)
                if c in ['u','d']:
                    cc = c
                else:
                    cc = '-'
                U,print_lines = oD(ud=cc)
                cr(U)
                #clear_screen()
                if str_is_int(c):
                    i = int(c)
                    cb(i)
                #i = input_int('>>> ')
                    if i in U:
                        if U[i]['lst_indx'] is None:
                            print(i,U[i])
                            cm(oD(U[i]['path']))
                        else:
                            print(i,U[i])
                            cy(oD('__meta__/menu_path/'))
                            if oD('__meta__/menu_path/'):

                                p = oD('__meta__/menu_path/')+ U[i]['path']
                            else:
                                p = U[i]['path']
                            cr(oD(p)[U[i]['lst_indx']])



            else:#except:
                print('oops!')


if False:
#############################
#,---a
    D = {} #.
    oD = dict_access(D,'D/') #.
    oD('a/b/c/d/e/',e=['x','y','z'],z=1) #.

    E = {} #.
    oE = dict_access(E,'E') #.
    oE('a/b/c/d/e/',e=2,z=1) #.

    oD(z=1)
    oE(z=1)

    oD('Y/',e=oE('a/'))#.
    oD(z=1)  #.
    #oD('a/b/c/d/',prune=1)
    oD(z=1) #.
    for i in range(3):
        print(i)
        #.
    raw_enter()
#,---b
#############################

#EOF

# ,b



