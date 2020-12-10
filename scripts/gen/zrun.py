#!/usr/bin/env python3

from k3.utils import *

A = get_Arguments({
	('positional_args', "project start code, must end in 'a'") : str,
},__file__)

A['p'] = A['positional_args']

assert(A['p'][-1] == 'a')

start = '#,'+A['p']
stop = start[:-1] + 'b'

tx = opjD('__temp__.txt')
os_system("rm",tx,"; python3 k3/scripts/gen/kgrep.py",qtd(start),">",tx)
g = txt_file_to_list_of_strings(tx)

fs = []
for h in g:
    if len(h) > 0:
        f = h.split(':')[0]
        fs.append(f)
f = select_from_list(fs)
c = get_code_snippet_(f,start=start,stop=stop)
if len(c) == 0:
	c = get_code_snippet_(f,start='"""'+start,stop=stop+'"""')
if len(c) == 0:
	cE('no code snippet found')
	sys.exit()

clear_screen()

d = c.split('\n')
l = []
for e in d:
    if len(e) > 0:
        if e[0] == ' ' or e[0].isalpha():
            l.append(e) 
clp(' zrun.py running',f+' ','`wbb')
c = '\n'.join(l)
if 'python ' in c:
	cr("*** warning, 'python' instead of 'python3' found",r=1)
os_system(c,e=1,a=1)

