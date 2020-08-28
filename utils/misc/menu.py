
from k3.utils.misc.zprint import *

offset = '\n───> '
offset = '\n     '

def set_str(dst_kc):
    kp = cf(*dst_kc,s0='/')
    v = input(d2s(offset+'Enter str for',kp))
    da(*dst_kc,e=v)  
    return d2s(offset,kp,'set to',da(*dst_kc))


def set_number(dst_kc,min_kc,max_kc):

    mn = da(*min_kc)
    assert(is_number(mn))
    mx = da(*max_kc)
    assert(is_number(mx))

    kp = cf(*dst_kc,s0='/')

    target_type = type(da(*dst_kc))

    v = input(d2s(offset+'Enter',target_type.__name__,'for',kp,'in range',(mn,mx),'> '))

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
        return d2s(offset+'failed to set',kp,'to',v)

    if v < mn or v > mx:
        return d2s(offset,v,'not in range',(mn,mx))

    da(*dst_kc,e=v)
            
    return d2s(offset+kp,'set to',da(*dst_kc))


def input_int(s='> '):
    c = input(s)
    if str_is_int(c):
        return int(c),c
    else:
        return None,c


def input_int_in_range(a,b,s):
    c,d = input_int(s)
    if c is None:
        return c,d
    if c < a or c > b:
        return None,d
    return c,d


def list_select_(lst):
    for i in rlen(lst):
        clp('    ',i,') ',lst[i],s0='')
    i,_ = input_int_in_range(0,len(lst)-1,offset+'>> ')
    return i


def list_select(dst_kc,options_kc):
    for i in rlen(da(*options_kc)):
        clp('    ',i,') ',da(*options_kc)[i],s0='')

    i,_ = input_int_in_range(0,len(da(*options_kc))-1,offset+'>> ')
    if i is None:
        return offset+'failed'

    da(*dst_kc,e=(da(*options_kc)[i]))
    return offset+'okay'

def toggle(kc):
    da(*kc,e=not da(*kc))
    message = d2s(offset+'toggled','/'.join(kc),'to',da(*kc))
    return message


def print_menu(top,ignore_underscore=True,ignore_keys=['options'],max_depth=999999):

    D, print_lines = zprint(
        da(*top),#ENV.D['menu'],
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
        #clp([D[i]],'in',[curmax,curmin,tog,curword,])
        if top[:-1]+D[i] in [curmax,curmin,tog,curword,]:
            V[ctr] = top[:-1]+D[i]
            print_lines[i+1] += cf(' (',ctr,')','`m',s0='')
            ctr += 1
    clear_screen()
    print('\n'.join(print_lines))
    return V


max_depth = 999999

if __name__ == '__main__':
        
    if 'setup menu':
        _words = ['cat','toggle','range','horse']
        _menu = {
            'range':{
                'min':{
                    'current':0,
                    #'_min':0,
                    #'_max':10,
                },
                'max':{
                    'current':10,
                    #'_min':0,
                    #'_max':10,
                },
                '_min':0,
                '_max':10,
            },
            'toggle':False,
            'word': {
                'current':_words[-1],
                '_options':_words,
            }   
        }
        ENV.D['menu'] = _menu


    if 'setup keychains':
        a = ['menu','range']
        curmax = a+['max','current']
        #maxmax = a+['max','_max']
        #maxmin = a+['max','_min']
        maxmax = a+['_max']
        maxmin = a+['_min']
        curmin = a+['min','current']
        minmax = maxmax#a+['min','_max']
        minmin = maxmin#a+['min','_min']
        tog = ['menu','toggle']
        a = ['menu','word']
        curword = a+['current']
        woptions = a+['_options']





    message = ''
    top = ['menu']

    targets = ['menu','menu/range','menu/word']

    while True:

        V = print_menu(
            top,
            ignore_underscore=da(*tog),
            ignore_keys=[da(*curword)],
            max_depth=max_depth,
        )

        print(message)

        if True:#try:
            c = input('> ')
            if c == 'q':
                break

            elif c == 'm':
                m,_ = input_int('enter max_depth > ')
                if type(m) is int and m > 0:
                    max_depth = m

            elif c == 'j':
                done = False
                while done == False:
                    p = input('enter new path > ')
                    if p[-1] == '/':
                        print(kys(da(*(p[:-1].split('/')))))
                    else:
                        done = True
                top = p.split('/')

            elif c == 't':
                i = list_select_(targets)
                top = targets[i].split('/')

            elif c == 'u':
                if len(top) > 1:
                    top.pop()
                    message = "went up"
                else:
                    message = "already at the top"

            elif c == 'd':
                if type(da(*top)) is not dict:
                    message = "can't go down"
                else:
                    i = list_select_(kys(da(*top)))
                    if i is None:
                        message = 'invalid selection'
                    else:
                        top.append(kys(da(*top))[i])
                        message = 'went down to '+top[-1]

            elif str_is_int(c):
                i = int(c)
                if i in V:
                    kc = V[i]
                    kp = cf(*kc,s0='/')

                    if kc == curmax:
                        message = set_number(curmax,maxmin,maxmax)

                    elif kc == curmin:
                        message = set_number(curmin,minmin,minmax)    
     
                    elif kc == tog:
                        message = toggle(kc)
                        #da(*kc,e=not da(*kc))
                        #message = d2s(offset+'toggled','/'.join(kc),'to',da(*kc))

                    elif kc == curword:
                        message = list_select(curword,woptions)
                                        
                else:
                    message = d2s(i,'is not a valid index')
            else:
                message = ''
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
