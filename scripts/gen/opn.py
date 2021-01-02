#!/usr/bin/env python3

from k3.utils import *


A = get_Arguments({
    ('p', 'paths')     : '[]',
})

exec('paths = '+A['p'])

if len(sggo(paths[0])) == 1:
    os_system('open',paths[0])


#EOF

