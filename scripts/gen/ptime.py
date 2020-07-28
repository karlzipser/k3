#!/usr/bin/env python
from k3.utils3 import *

s = time_str('Pretty2')




print('\n'+s+'\n')



try:
	setClipboardData(s)
	cy("\t'"+s+"'",'in clipboard.')
except:
	cr("\t'"+s+"'",'NOT in clipboard.')

#EOF