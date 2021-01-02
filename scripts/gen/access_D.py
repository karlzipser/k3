#!/usr/bin/env python3

from k3.utils import *


A = get_Arguments({
    'p' : 'sf_output',
    'i' : -1,
})

try:
    D = loD('D')
except:
    cE('D not found')
    sys.exit()

o = D[A['p']][A['i']]
#o = o
print(o)
print(o,stdout=True)


#EOF

