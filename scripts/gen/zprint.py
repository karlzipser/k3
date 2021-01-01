#!/usr/bin/env python3

from k3.utils import *


A = get_Arguments({
    ('p', 'path')     : opjD('D'),
    ('v', 'variable path') : '',
})

D = loD('D')

if A['v'] == '':
    zprint(D,t=A['p'])

else:

    v,vt = A['v'],A['v']

    if v[-1] != '/':
        v = v + '/'

    if vt[-1] == '/':
        vt = vt[:-1]

    oD = dict_access(D,opj(A['p']+vt))

    oD(v,z=1)


#EOF

