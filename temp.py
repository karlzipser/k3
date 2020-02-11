from __future__ import print_function
from __future__ import division

from k3.utils import *



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
    print('sum = '+str(s))
    return s

if __name__ == '__main__':
    Arguments = args_to_Arguments(sys.argv[1:])
    add_args(Arguments)

    
#EOF
