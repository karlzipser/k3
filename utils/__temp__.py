#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

def add_args(A):
    """
    e.g.,
        python k3/temp.py --a 1 --b 2 --c 3 --d 4
    """
    s = 0
    for k in A:
        a = A[k]
        assert(type(a) == int)
        s += a
    print('Sum = '+str(s))
    return s





#EOF
