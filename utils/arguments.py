from __future__ import print_function
from __future__ import division

from printing import *
from bools import *

def args_to_Arguments0(*args):
    if not is_even(len(args[0])):
        print("args_to_dictionary(*args)")
        print("args are:")
        print(args)
        print('def args_to_dictionary(*args): Warning, not is_even(len(args[0]))')
        return
    ctr = 0
    keys = []
    values = []
    for e in args[0]:
        if is_even(ctr):
            assert(len(e) != 3)
            if len(e) == 2:
                assert(e[0] == '-')
                assert(e[1] != '-')
                assert(not str_is_int(e[1]))
                keys.append(e[1])
            else:
                assert(e[:2] == '--')
                assert(e[2] != '-')
                keys.append(e[2:])
        else:
            assert(e[:2] != '--')
            if str_is_int(e):
                v = int(e)
            elif ',' in e:
                v = e.split(',')
            elif e == 'True':
                v = True
            elif e == 'False':
                v = False        
            else:
                v = e
            values.append(v)
        ctr += 1
    Arguments = {}
    if len(keys) != len(values):
        print("args_to_dictionary0(*args)")
        print("given keys are:")
        print(keys)
        print("given values are:")
        print(values)
        raise ValueError('ERROR because: len(keys) != len(values)')
    for k,v in zip(keys,values):
        Arguments[k] = v
    return Arguments

if __name__ == '__main__':
    Arguments = args_to_Arguments0(sys.argv[1:])
    print(Arguments)
    # e.g.,
    #   python k3/utils/arguments.py --a b,c,d,1 --t True --f 1 --q 0.123
    # returns
    #   {'a': ['b', 'c', 'd','1'], 'q': '0.123', 't': True, 'f': 1}
    
#EOF
