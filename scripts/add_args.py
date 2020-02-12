#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

from k3.utils import *



def add_args(A):
    """
    e.g.,
        k3/scripts/add_args.py -a 1 -b 2 --cat 3 --dog 4
    """
    Required_arguments = {
        'a':int,
        'b':int,
        'cat':int,
        'dog':int,
    }
    Default_values = {
        'monkey':9,
        'snake':-3,
    }
    valid_keys = Required_arguments.keys() + Default_values.keys()

    for k in A:
        assert k in valid_keys
        a = A[k]
        assert(type(a) == int)
    s = A['a'] + 2*A['b'] - 3*A['cat'] + 4*A['dog']
    print(A)
    print('sum = '+str(s))
    return s

if __name__ == '__main__':
    Arguments = args_to_Arguments(sys.argv[1:])
    add_args(Arguments)

    
#EOF
