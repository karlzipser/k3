#!/usr/bin/env python3

from k3.utils import *


A = get_Arguments({
    ('p', 'start path')     : opjh(),
    ('v', 'variable name') : 'sf_output',
    ('a', 'append') : False,
})

try:
    D = loD('D')
except:
    D = {}

if 'select_files.py' in __file__:
    f = select_files

if 'select_file.py' in __file__:
    f = select_file

if 'select_folders.py' in __file__:
    f = select_folders

if 'select_folder.py' in __file__:
    f = select_folder

l = f(A['p'])

v = A['v']

if A['a']:
	if v not in D:
		D[v] = []
	D[v] += l
else:
	D[v] = l

soD(D,'D')


#EOF

