#,a

from k3.utils.misc.zprint import *


def o_base(D):
    
    D['__menu_path__'] = None

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
    ):
        if p == '':
            p = None

        if m is not None:
            assert_as(p is None,"p is None")
            p = D['__menu_path__']
            m = None


        def _zprint(z,p,D,t,k):
            if z:
                if t is None: t = p
                zprint(D,t)


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
                _zprint(z,p,D,t,key_list)
            else:
                _zprint(z,p,D,'','')

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
            _zprint(z,p,D,t,k)
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


if __name__ == '__main__':
 
    code = """

clear_screen()

if '__file__' in locals(): eg(__file__)

import copy

D = {}
oD = o_base(D)
oD('a/b/c/d/e/',e=1,z=1)

E = {}
oE = o_base(E)
oE('a/b/c/d/e/',e=2,z=1)

oD(z=1)
oE(z=1)

oD('Y/',e=oE('a/'))
oD(z=1)  
oD('a/',prune=1)
oD(z=1)

    """

    for c in code.split('\n'):
        if not c.isspace():
            clp(c,'`--u')
            exec(c)


if False:
    if ud == -1:
        if D['__menu_path__'] == None:
            #_message("already at top")
            #return o() ###################
            pass
        D['__menu_path__'] = pname_(
            D['__menu_path__']
        ) + '/'
        #_message('went up to '+Environment['current_prefix_path'])

    elif ud == 1:
        key_list = Environment['current_prefix_path'][:-1].split('/')
        D = Environment['dictionary']
        for k in key_list:
            k = str_to_tuple_as_necessary(k)
            D = D[k]
        if type(D) == dict:
            if has_form_of_alias(d):
                if d in kys(D):
                    Environment['current_prefix_path'] += d + '/'
                    _message(d2s('down to',d))
                    return o() ###################
                else:
                    assert False
            if len(kys(D)) > 1:
                k = select_from_list(kys(D))
            else:
                k = kys(D)[0]
            Environment['current_prefix_path'] += k + '/'
            _message(d2s('down to',k))
        else:
            _message("can't go down")
        return o() ###################
    elif d is None:
        pass

    else:
        assert False
#EOF

#,b



