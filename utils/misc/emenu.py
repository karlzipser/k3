
from k3.utils.misc.zprint import *
from k3.utils.misc.sys import *
from k3.utils.vis import *
from k3.utils.misc.environment import *



if 'functions to set dict values':

    def set_str(path):
        s='Enter str for'
        v = input(d2s(s,qtd(path),'> '))
        o(path,e=v)  
        return d2s(qtd(path),'set to',o(path))


    def set_number(dst_path,mn,mx):

        assert(is_number(mn))
        assert(is_number(mx))

        target_type = type(o(dst_path))

        v = input(d2s('Enter',target_type.__name__,'for',qtd(dst_path),'in range',(mn,mx),'> '))

        no = False

        if target_type == int:

            if str_is_int(v):
                v = int(v)
            else:
                no = True

        elif target_type == float:
            if str_is_float(v):
                v = float(v)
            else:
                no = True
        else:
            no = True

        if no:
            return d2s('failed to set',qtd(dst_path),'to',v)

        if v < mn or v > mx:
            return d2s(v,'not in range',(mn,mx))

        o(dst_path,e=v)
                
        return d2s(qtd(dst_path),'set to',o(dst_path))


    def set_from_list(dst_path,options_path):

        for i in rlen(di(options_path)):
            clp('    ',i,') ',di(options_path)[i],s0='')

        i = input_int_in_range(0,len(di(options_path))-1,'>> ')
        if i is None:
            return 'failed'

        o(dst_path,e=(o(options_path)[i]))
        return d2s(qtd(dst_path),'set to',di(dst_path))


    def set_toggle(path):
        o(path,e=not o(path))
        message = d2s('toggled',qtd(path),'to',di(path))
        return message


"""
def dip(path):
    clp(fname(path)+':',di(path))


def print_menu(
    top,
    ignore_underscore=True,
    ignore_keys=['options'],
    max_depth=10000,action_paths=[],
):
    top = top.split('/')
    D, print_lines = zprint(
        da(*top),
        t=top[-1],
        use_color=True,
        use_line_numbers=False,
        ignore_underscore=ignore_underscore,
        do_return=True,
        do_print=False,
        ignore_keys=ignore_keys,
        max_depth=max_depth,
    )
    for i in kys(D):
        if i+1 in D:
            if D[i] == D[i+1]:
                D[i+1].append('---')
    V = {}
    ctr = 1
    for i in kys(D):
        d = []
        for a in top[:-1]+D[i]:
            d.append(str(a))
        p = '/'.join(d)
        if p in action_paths:
            V[ctr] = p
            print_lines[i+1] += cf(' (',ctr,')','`m',s0='')
            ctr += 1
    clear_screen()

    print('\n'.join(print_lines))

    return V,D



def test_for_valid_path(path):
    try:
        di(path)
        return True
    except:
        return False


max_depth = 5
"""




#if __name__ == '__main__':

#    eg(__file__)
        

_words = ['cat','dog','bird','horse']


Environment['dictionary']['~']['menu'] = {
    'range':{
        'min':{
            'value':0,
            '_function':set_number,
            '_args': ['menu/range/_min/','menu/range/_max/'],
        },
        'max':{
            'value':10,
            '_function':set_number,
            '_args': ['menu/range/_min/','menu/range/_max/'], 
        },
        '_min':0,
        '_max':10,
    },
    'set_toggle':{
        'value':False,
        '_function':set_toggle,
    },
    'word': {
        'value':_words[-1],
        '_function':set_from_list,
        '_args':['menu/word/_options'],
        '_options':_words,
    },
    'str': {
        'value':'This is a string.',
        '_function':set_str,
    },
       
}

del _words
 
zprint(Environment)
print(o('menu/range/_max/'))
o(pm=1)
zprint(o())#,t='2')
print(o('menu/range/_max/',e=5))
o(pm=1)
zprint(o(),ignore_underscore=True)#,t='2')
"""



    message = ''

    top = 'menu'

    targets = ['menu','menu/range','menu/word']



    while True:

        V,D_ = print_menu(
            top,
            ignore_underscore=di('menu/set_toggle'),
            ignore_keys=[],
            max_depth=max_depth,
            action_paths=kys(Actions),
        )

        clp(message,r=0)

        if True:#try:
            c = input('> ')

            if c == 'q':
                break

            elif c == 'm':
                m = input_int('enter max_depth > ')
                if type(m) is int and m > 0:
                    max_depth = m

            elif c == 'j':
                done = False
                while done == False:
                    p = input('enter new path > ')
                    if p[-1] == '/':
                        if test_for_valid_path(p):
                            print(kys(da(*(p[:-1].split('/')))))
                            message = d2s(p,'is valid')
                        else:
                            message = d2s(p,'is not a good path')
                    else:
                        done = True
                t = p.split('/')
                if test_for_valid_path(p):
                    q = da(*t)
                    top = t
                    message = d2s(p,'is valid')
                else:
                    message = d2s(p,'is not a good path')

            elif c == 't':
                i = select_from_list(targets)
                top = targets[i]

            elif c == 'u':
                if len(top.split('/')) > 1:
                    top = '/'.join(top.split('/')[:-1])
                    message = "went up"
                else:
                    message = "already at the top"

            elif c == 'd':
                toplist = top.split('/')
                if type(da(*toplist)) is not dict:
                    message = "can't go down"
                else:
                    i = select_from_list(kys(da(*toplist)))
                    if i is None:
                        message = 'invalid selection'
                    else:
                        toplist.append(kys(da(*toplist))[i])
                        message = 'went down to '+toplist[-1]
                top = '/'.join(toplist)

            elif str_is_int(c):
                i = int(c)
                if i in V:
                    kc = V[i]
                    print(kc)
                    X = Actions[kc]
                    a,b = None,None
                    if len(X['args']) > 0:
                        a = X['args'][0]
                    if len(X['args']) > 1:
                        b = X['args'][1]

                    message = X['function'](kc,a,b)


                                        
                else:
                    message = d2s(i,'is not a valid index')
            else:
                message = ''
"""
"""
except KeyboardInterrupt:
    cE('*** KeyboardInterrupt ***')
    sys.exit()
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    message = cf('Exception:',exc_type,file_name,exc_tb.tb_lineno,'`rwb')        
"""




#EOF
