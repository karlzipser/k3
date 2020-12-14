#!/usr/bin/env python3

from k3.utils import *

A = get_Arguments({
	('txt', 'warning text') : "Move now, stop sitting in one place!",
	('title','dialogue title') :'Warning!',
	('min', 'repeat every --min minutes')        : 15,
})
A_={
	'txt' : "Move now, stop sitting in one place!",
	'title' :'Warning!',
	'min'        : 10.,
}
while True:
	time.sleep(A['min']*60)
	#cm(0)
	os_system("osascript -e 'Tell application \"System Events\" to display dialog",qtd(A['txt']),"with title \""+A['title']+"\"'")
	#cm(1)

#EOF
