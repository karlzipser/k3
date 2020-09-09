
from k3.utils.core.printing import *


def input_int(s='> '):
    c = input(s)
    if str_is_int(c):
        return int(c)
    else:
        return None

def input_from_choices(s='> ',choices=[]):
    c = input(s)
    if str_is_int(c):
        c = int(c)
    if c in choices:
        return c
    else:
        return None

def input_int_in_range(a,b,s):
    c = input_int(s)
    if c is None or c < a or c > b:
        return None
    else:
        return c

def select_from_list(lst,ignore_underscore=False):
    ctr = 0
    for i in rlen(lst):
        if True:#ignore_underscore and lst[i][0] != '_':
            clp('    ',i,') ',lst[i],s0='')
            ctr += 1
    if ctr > 1:
        i = input_int_in_range(0,len(lst)-1,'>> ')
    else:
        i = 0
    if i is None:
        return None
    return lst[i]

#EOF
