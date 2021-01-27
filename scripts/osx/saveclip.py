#!/usr/bin/env python3

from k3.utils import *

record_PID(__file__,just_one=True)


A = get_Arguments(
	{
		'dst' : opjD('_clipboards.txt'),
		'delimiter' : '\n<====>\n',
		't' : 0.333,
    },
    verbose=True,
    file=__file__,
)
exec(A_to_vars_exec_str)


try:
	clipboards = file_to_text(dst_).split(delimiter_)
except:
	clipboards = []


while True:

	c = getClipboardData()

	if len(clipboards) == 0 or c != clipboards[-1]:
		if c in clipboards:
			clipboards.remove(c)
		clipboards.append(c)
		text_to_file(dst_,delimiter_.join(clipboards))
		print('wrote to',dst_)

	time.sleep(t_)


#EOF
