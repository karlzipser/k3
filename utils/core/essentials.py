
from k3.utils.core.imports import *


def intr(n):
    return np.int(np.round(n))


def as_pct(a,b):
    return d2n(intr(100*a/b),'%')


def qtd(a):
    return '\"'+a+'\"'
    

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
        
#EOF
