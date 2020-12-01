#!/usr/bin/env python3

import sys, os

args = ' '.join(sys.argv[1:])

print('\n')

os.system('grep -r -n ' + '"'+args+'"' + ' k3')

#EOF
