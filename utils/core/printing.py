
from k3.utils.core import *

from termcolor import cprint
from termcolor import colored

def print_dic_simple(D,title=''):
    print(title)
    if type(D) is not dict:
        print(D)
    else:
        for k in D:
            pd2s('   ',k+':',D[k])

def d2s_spacer(args,spacer=' '):
    lst = []
    for e in args:
        try:
            ee = str(e)
        except:
            ee = e
            #print('d2s_spacer except with '+ee)
        lst.append(ee)
    return spacer.join(lst)


def d2s(*args):
    '''
    e.g.,
    
    d2s('I','like',1,'or',[2,3,4])
    
    yields
    
    'I like 1 or [2, 3, 4]'
    
    d2c(1,2,3) => '1,2,3'
    d2f('/',1,2,3) => '1/2/3'
    '''
    return d2s_spacer(args)

def d2c(*args):
    return d2s_spacer(args,spacer=',')

def d2p(*args):
    return d2s_spacer(args,spacer='.')

def d2n(*args):
    return d2s_spacer(args,spacer='')

def d2f(*args):
    return d2s_spacer(args[1:],spacer=args[0])

def pd2s(*args):
    print(d2s(*args))

def pd2n(*args):
    print(d2n(*args))

def beep():
    print('\007')

def dp(f,n=2):
    """
    get floats to the right number of decimal places, for display purposes
    """
    assert(n>=0)
    if n == 0:
        return int(np.round(f))
    f *= 10.0**n
    f = int(np.round(f))
    return f/(10.0**n)

def clear_screen():
    print(chr(27) + "[2J")




def et():
    print(
        """
except KeyboardInterrupt:
    cr('\n\n*** KeyboardInterrupt ***\n')
    sys.exit()
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print('Exception!',emphasis=True)
    print(d2s(exc_type,file_name,exc_tb.tb_lineno),emphasis=False)        

        """
)



cstr = """
def cQ(*args,**kwargs):
    cprint(d2s_spacer(tuple(list(args)),spacer=' '),'COLOR')
    if k_in_D('ra',kwargs) or k_in_D('r',kwargs):
        cprint('\b  (hit Enter to continue)','COLOR')
        raw_input()
    if k_in_D('t',kwargs):
        time.sleep(kwargs['t'])
"""

for color in ['red','yellow','green','blue','magenta','cyan','white','Grey']:
    an_exec_string = cstr.replace('Q',color[0]).replace('COLOR',color).replace('Grey','grey')
    exec(an_exec_string)






# minor



def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows),int(columns)


def format_row(list_of_sym_percent_pairs):
    __,ncols = get_terminal_size()
    row_str = ''
    for i in range(ncols):
        for sp in list_of_sym_percent_pairs:
            sym = sp[0]
            per = sp[1]
            if per < 0:
                per = 0.
            elif per > 99:
                per = 99.
            col = int(per/100.*ncols)
            if i == col:
                row_str += sym
                break
        else:
            row_str += ' '
    return row_str


rd = '\x1b[31m'
gr = '\x1b[32m'
yl = '\x1b[33m'
bl = '\x1b[34m'
mg = '\x1b[35m'
lb = '\x1b[36m'
wh = '\x1b[37m'

wh_bk = '\x1b[40m'
wh_rd = '\x1b[41m'
wh_gr = '\x1b[42m'
wh_bl = '\x1b[44m'
wh_mg = '\x1b[45m'
wh_lb = '\x1b[46m'

mg = '\x1b[35m'
lb = '\x1b[36m'
wh = '\x1b[37m'

og = '\x1b[91m'
underlined = '\x1b[4m'



#EOF
