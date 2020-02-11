from __future__ import print_function
from __future__ import division

from renaming import *

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

def has_even_length(d):
    l = d['l']
    return np.mod(len(l),2) == 0




