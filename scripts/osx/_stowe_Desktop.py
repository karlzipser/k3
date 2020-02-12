#!/usr/bin/env python
from __future__ import print_function
from __future__ import division

from k3.utils import *
import argparse

_INVALID_DEFAULT = '__nada__'
_parser = argparse.ArgumentParser(description='stowe_Desktop')
_parser.add_argument('dst', nargs='?',action="store", type=str,default=_INVALID_DEFAULT,help='dst')

_results = _parser.parse_args()

def stowe_Desktop(dst=False):
    if dst==False:
        dst = opjh('Desktops_older','Desktop_'+time_str())
    print(dst)
    os.system('mkdir -p ' + dst)
    _,l = dir_as_dic_and_list(opjD(''))
    for i in l:
        shutil.move(opjD(i),dst)

if __name__ == '__main__':
	if _results.dst == _INVALID_DEFAULT:
		stowe_Desktop()
	else:
		stowe_Desktop(_results.dst)

#EOF


