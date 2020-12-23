#!/usr/bin/env python3

from k3.utils import *

startfiles = [
	"scripts/gen/bkp.py",
	"scripts/osx/warn.py"
]

for s in startfiles:
	
	os_system('python3',opjk(s),'&')

#EOF
