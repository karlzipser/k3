from __future__ import print_function
from __future__ import division

from k3.utils import *

def print_A(A):
    print('print_A')
    print(A)

if __name__ == '__main__':
    Arguments = args_to_Arguments(sys.argv[1:])
    print_A(Arguments)
    # e.g.,
    #   python k3/temp.py --a b,c,d,1 --t True --f 1 --q 0.123
    # returns
    #   {'a': ['b', 'c', 'd','1'], 'q': '0.123', 't': True, 'f': 1}
    
#EOF
