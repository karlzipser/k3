#!/usr/bin/env python3

from k3.utils.misc.printing import *
#,a


def input_something(name,current):

    assert name is not None
    assert current is not None

    type_ = type(current)

    if type(name) is str:
        istr = 'enter value for '+name+' > '
    else:
        istr = 'enter value > '

    if type_ is bool:
        return not current

    else:
        v = input('enter value for '+name+' > ')
        
        if type_ is int:
            if str_is_int(v):
                v = int(v)
                return v
            else:
                return None

        elif type_ is float:
            if str_is_float(v):
                v = float(v)
                return v
            else:
                return None

        elif type_ is str:
            return v

        else:
            return None





def mini_menu(A,clear=True,menu_name='MINI MEUNU'):

    while True:

        try:

            if clear:
                clear_screen()

            clp(menu_name,'`w-bu','(ctr-C to exit)','`w-d')

            ks = sorted(kys(A))
            for i in rlen(ks):
                k = ks[i]
                s = A[k]
                if type(s) in [int,float,bool]:
                    pass
                elif type(s) is str:
                    s = qtd(s)
                elif type(s) is dict:
                    s = '<dict>'
                elif type(s) is list:
                    s = '<list>'
                elif type(s) is tuple:
                    s = '<tuple>'
                else:
                    s = '<other>'

                clp(d2n(i,') ',k,' ='),'`w--',s,'`w-b')

            n = input_int_in_range(0,len(ks),'# ? ')

            if n is None:
                continue

            k = ks[n]
            #cm(n,k)

            if n is None:
                continue
            #cg(k,A[k])
            m = input_something(k,A[k])

            #cy(m)

            if m is not None:
                A[k] = m
            else:
                cE('failed to update',k,r=1)

        except KeyboardInterrupt:
            cb('leaving mini_menu')
            break

if False:
    A={
        'path':'k3',
        'condense_dict':False,
        'ignore_meta':{1:2},
        'max_depth':[1,2,3],
        'preview_x':0,
        'preview_y':(1,2,3),
        'preview_h':250,
        'preview_w':500,
    }
    while True:
        mini_menu(A)
        cm(0,r=1)

#,b



#EOF