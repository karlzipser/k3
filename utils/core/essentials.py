
from k3.utils.core.imports import *


def clear_screen():
    print(chr(27) + "[2J")
    
def eg(file,cs=True):
    if cs:
        clear_screen()
    print('Examples from '+file+':')
    print('') 



def intr(n):
    return np.int(np.round(n))


def as_pct(a,b):
    return d2n(intr(100*a/b),'%')



def qtd(a):
    if (a[0] == '\'' and a[-1] == '\'') or (a[0] == '\"' and a[-1] == '\"'):
        print('*** qtd(): Warning, '+a+' seems to be quoted already ***')
    return '\"'+str(a)+'\"'
    

def raw_enter(optional_str=''):
    return input(optional_str+'   Hit enter to continue > ')


def is_even(q):
    if np.mod(q,2) == 0:
        return True
    return False
    
def str_is_int(s):
    try:
        int(s)
        return True
    except:
        return False

def str_is_float(s):
    try:
        float(s)
        return True
    except:
        return False

def rlen(a):
    return range(len(a))


def atoi(text):
    return int(text) if text.isdigit() else text


def getch():
    import sys, termios, tty, os, time
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def k_in_D(k,D):
    if k not in D:
        return False
    else:
        return D[k]


def is_number(n):
    if type(n) == bool:
        return False
    if type(n) == type(None):
        return False
    return isinstance(n,numbers.Number)


def bound_value(the_value,the_min,the_max):
    if the_value > the_max:
        return the_max
    elif the_value < the_min:
        return the_min
    else:
        return the_value


def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

#EOF
