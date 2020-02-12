#!/usr/bin/env python
from __future__ import print_function
from __future__ import division

from k3.utils import *
import argparse

_INVALID_DEFAULT = '__nada__'


def stowe_Desktop(A):

    if SCRATCH:
        assign_defauts(
            A,
            Required_arguments={
                ('dir','d'): str,},
            Default_values={
                ('path','p'): opjh('Desktops_older'),
            },
        )


    dst = opjh(A['path'],'Desktop_'+time_str())
    print(dst)
    os.system('mkdir -p ' + dst)
    _,l = dir_as_dic_and_list(opjD(''))
    for i in l:
        shutil.move(opjD(i),dst)



if __name__ == '__main__':
    A = args_to_Arguments0(sys.argv[1:])
    stowe_Desktop(A)


#EOF





