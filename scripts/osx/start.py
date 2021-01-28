#!/usr/bin/env python3

from k3.utils import *

record_PID(__file__,just_one=True)

startfiles = [
	"scripts/gen/bkp.py",
	"scripts/osx/warn.py",
	"scripts/osx/saveclip.py",
]

for s in startfiles:
	
	os_system('python3',opjk(s),'&')

if True:
	if not os.path.exists(opjh('.activity')):
		os_system('touch', opjh('.activity'))


	s = """watchmedo shell-command \
	    --patterns="*.py;*.txt;*.rtf;*.jpg;*.jpeg;*.png" \
	    --recursive \
	    --command='echo "${watch_src_path}";touch .activity' \
	    k3 Desktop
	"""
	os_system(s,'&',e=1)


#EOF
