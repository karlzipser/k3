from k3 import *


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