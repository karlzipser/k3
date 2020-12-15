#!/usr/bin/env python3

from k3.utils import *

#print(__file__)

path = should_I_start(__file__)

os_system('python3 k3/scripts/gen/bkp.py &') 
os_system('python3 k3/scripts/osx/warn.py &') 


starttime = time.time()

while True:
	for i in range(6):
		if True:
			print(dp(time.time() - starttime))
			os_system('touch',path,e=1)
		time.sleep(10)

#EOF
