#!/usr/bin/env python
from __future__ import print_function
from __future__ import division

from k3.utils import *
import argparse

_INVALID_DEFAULT = '__nada__'
_parser = argparse.ArgumentParser(description='restore_Desktop')
_parser.add_argument('src', nargs='?',action="store", type=str,default=_INVALID_DEFAULT,help='src folder')

_results = _parser.parse_args()



def restore_Desktop(src):
    src = opjh('Desktops_older',src)
    _,l = dir_as_dic_and_list(opjD())
    if len(l) > 0:
        print('*** Cannot restore Desktop because Desktop is not empty ***')
        return False
    _,l = dir_as_dic_and_list(src)
    for i in l:
        shutil.move(opjh(src,i),opjD())

if __name__ == '__main__':
    
    if _results.src == _INVALID_DEFAULT:
        print('*** Need to give src folder within ~/Desktops_older ***')
    else:
        restore_Desktop(_results.src)

#EOF
