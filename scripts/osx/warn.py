#!/usr/bin/env python3

from k3.utils import *

print(__file__)

#path = should_I_start(__file__)

#os_system('python3 k3/scripts/gen/bkp.py &') 

A = get_Arguments({
	('txt', 'warning text') : "Move now, stop sitting in one place!",
	('title','dialogue title') :'Warning!',
	('min', 'repeat every --min minutes')        : 15,
})

#starttime = time.time()

print('warning...')
while True:

	for i in range(A['min']*60):
		time.sleep(1)
	os_system("osascript -e 'Tell application \"System Events\" to display dialog",qtd(A['txt']),"with title \""+A['title']+"\"'")

#EOF
