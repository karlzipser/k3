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



names = [
    'apple',
    'pear',
    'x',
    'y',
    'z',
]
names = list(set(names))
for s in names:
    locals()[s+'_'] = s
del names



def assign_defaults(Arguments,required_keys,Defaults):
    for k in required_keys:
        assert k in Arguments
        assert k not in Defaults
    for k in Defaults:
        if k not in Arguments:
            Arguments[k] = Defaults[k]

A = {apple_:1,pear_:2}

def test(A,r={}):
    assign_defaults(A,[apple_,pear_],{z_:3},)
    kprint(A,title='A',r=r)

test(A)



#EOF
