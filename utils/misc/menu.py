
from k3.utils.misc.zprint import *

def set_str(dst_kc):
    kp = cf(*dst_kc,s0='/')
    v = input(d2s('    Enter str for',kp))
    da(*dst_kc,e=v)  
    return d2s('    ',kp,'set to',da(*dst_kc))


def set_number(dst_kc,min_kc,max_kc):

    mn = da(*min_kc)
    assert(is_number(mn))
    mx = da(*max_kc)
    assert(is_number(mx))

    kp = cf(*dst_kc,s0='/')

    target_type = type(da(*dst_kc))

    v = input(d2s('    Enter',target_type.__name__,'for',kp,'in range',(mn,mx),'> '))

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
        return d2s('    failed to set',kp,'to',v)

    if v < mn or v > mx:
        return d2s('    ',v,'not in range',(mn,mx))

    da(*dst_kc,e=v)
            
    return d2s('    ',kp,'set to',da(*dst_kc))


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


def list_select(dst_kc,options_kc):
    i,_ = input_int_in_range(0,len(da(*options_kc))-1,'    >> ')
    if i is None:
        return '    failed'

    da(*dst_kc,e=(da(*options_kc)[i]))
    return '    okay'





if __name__ == '__main__':
        
    if 'setup menu':
        _words = ['cat','dog','mouse','horse']
        _menu = {
            'range':{
                'min':{
                    'current':0,
                    'min':0,
                    'max':10,
                },
                'max':{
                    'current':10,
                    'min':0,
                    'max':10,
                },
            },
            'toggle':False,
            'word': {
                'current':_words[-1],
                'options':_words,
            }   
        }
        ENV.D['menu'] = _menu


    if 'setup keychains':
        a = ['menu','range']
        curmax = a+['max','current']
        maxmax = a+['max','max']
        maxmin = a+['max','min']
        curmin = a+['min','current']
        minmax = a+['min','max']
        minmin = a+['min','min']
        tog = ['menu','toggle']
        a = ['menu','word']
        curword = a+['current']
        woptions = a+['options']




    message = ''

    while True:

        D, print_lines = zprint(
            ENV.D['menu'],
            t='menu',
            use_color=True,
            use_line_numbers=False,
            do_return=True,
            do_print=False,
        )
        for i in kys(D):
            if i+1 in D:
                if D[i] == D[i+1]:
                    D[i+1].append('---')
        V = {}
        ctr = 1
        for i in kys(D):
            if D[i] in [curmax,curmin,tog,curword,]:
                V[ctr] = D[i]
                print_lines[i+1] += cf(' (',ctr,')','`m',s0='')
                ctr += 1

        clear_screen()
        print('\n'.join(print_lines))
        print(message)

        if True:#try:
            c = input('> ')
            if c == 'q':
                break
            if str_is_int(c):
                i = int(c)
                if i in V:
                    kc = V[i]
                    kp = cf(*kc,s0='/')

                    if kc == curmax:
                        message = set_number(curmax,maxmin,maxmax)

                    elif kc == curmin:
                        message = set_number(curmin,minmin,minmax)    
     
                    elif kc == tog:
                        da(*kc,e=not da(*kc))

                    elif kc == curword:
                        message = list_select(curword,woptions)
                                        
                else:
                    message = d2s(i,'is not a valid index')
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
