from __future__ import print_function
from __future__ import division

from termcolor import cprint
from termcolor import colored
from have import *

def d2s_spacer(args,spacer=' '):
    lst = []
    for e in args:
        lst.append(str(e))
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


def format_row(list_of_sym_percent_pairs):
    __,ncols = get_terminal_size()
    row_str = ''
    for i in range(ncols):
        for sp in list_of_sym_percent_pairs:
            sym = str(sp[0])
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


def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows),int(columns)



def raw_enter(optional_str=''):
    return raw_input(optional_str+'   Hit enter to continue > ')




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



#EOF
