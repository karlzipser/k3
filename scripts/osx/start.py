#!/usr/bin/env python3

from k3.utils import *

path = should_I_start(__file__)

cg(__file__)

startfiles = [
	"scripts/gen/bkp.py",
	"scripts/osx/warn.py"
]

for s in startfiles:
	os_system('python3',opjk(s),'&') 

starttime = time.time()

while True:
	for i in range(6):
		if True:
			cg('time since starttime =',datetime.timedelta(seconds=int(time.time() - starttime)))
			os_system('touch',path,e=1)
		time.sleep(30)


#EOF
