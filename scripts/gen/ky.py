#!/usr/bin/env python3

import sys, os

args = ' '.join(sys.argv[1:])
if len(args) == 0:
    args = "'<no args>'"

try:
    try:
        exec('out = ' + args)
    except:
        exec(args)
except:
    from k3 import *
    try:
        exec('out = ' + args)
    except:
        exec(args)
try:
    try:
        zprint(out,t=args)
    except:
        print('out:',out)
except:
    pass

#EOF
