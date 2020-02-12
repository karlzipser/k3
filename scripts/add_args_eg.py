#!/usr/bin/env python

from __future__ import print_function
from __future__ import division

from k3.utils import *



def add_args_eg(A):
    assign_defauts0(
        A,
        Required_arguments={
            'a':int,
            'b':int,
            'cat':int,
            'dog':int,},
        Default_values={
            'monkey':9,
            'snake':-3,},)
    
    for k in A:
        a = A[k]
        assert(type(a) == int)
    s = A['a'] + 2*A['b'] - 3*A['cat'] + 4*A['snake']
    print(A)
    print('sum = '+str(s))
    return s

if __name__ == '__main__':
    Arguments = args_to_Arguments0(sys.argv[1:])
    add_args_eg(Arguments)

    
#EOF
